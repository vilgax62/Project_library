from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages , admin
# from django.utils.safestring import mark_safe
# from django.contrib.admin.models import LogEntry
# from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from .models import Book, IssuedBook
from .serializers import BookSerializer



@csrf_exempt
@api_view(['POST'])
def register_user_api(request):

    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'message': 'User created successfully.', 'token': token.key}, status=status.HTTP_201_CREATED)

#   return Response({'token': token.key}, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Django HTML views
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            if request.method == 'POST':
                return redirect('login')  # redirect after POST!
    return render(request, 'login.html')


def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('login')


#register.html
def register_page(request):
    return render(request, 'register.html')

# admin page

class CustomUserAdmin(admin.ModelAdmin):
    change_form_template = 'admin/custom_user_change_form.html'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# browsebook.html
def browse_books_page(request):
    books = Book.objects.filter(is_available = True)
    return render(request, 'browse_book.html',{'books' : books})
# addtocart
def add_to_cart_page(request):
    return render(request,"add_cart.html")
# checkout
# def checkout_cart(request):
#     return render(request,"checkout.html")


def save_later(request):
    return render(request,"save-for-later.html")


# @staff_member_required
# def admin_dashboard(request):
#     return render(request, 'admin/admin_dashboard.html')
    # log_entries = LogEntry.objects.all().order_by('-action_time')[:10]  # last 10 logs
    # context = {
    #     'page_title': 'Admin Dashboard',
    #     'log_entries': log_entries,}
    # return render(request,"admin_dashboard.html" ) 


# index book api
# DRF API View
@api_view(['GET'])
def browse_books(request):
    sort_by = request.GET.get('sort')
    books = Book.objects.filter(is_available=True)

    if sort_by == 'most_issued':
        books = books.order_by('-issued_count')
    elif sort_by == 'least_issued':
        books = books.order_by('issued_count')
    elif sort_by == 'author':
        books = books.order_by('author')

    serializer = BookSerializer(books, many=True, context={'request': request})
    return Response(serializer.data)

from .models import Cart, Book

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    user = request.user
    book_id = request.data.get('book_id')

    try:
        book = Book.objects.get(id=book_id)
        cart, created = Cart.objects.get_or_create(user=user, book=book)
        return Response({"message": "Book added to cart"}, status=201)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

from datetime import timedelta
from django.utils import timezone
from .models import IssuedBook

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        return Response({'error': 'Cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)

    bill = []
    total = 0
    for item in cart_items:
        IssuedBook.objects.create(
            user=request.user,
            book=item.book,
            issue_date=timezone.now().date(),
            return_date=timezone.now().date() + timedelta(days=14),
            price=item.book.rent_price
        )
        item.book.issued_count += 1
        item.book.save()
        total += item.book.rent_price
        bill.append({
            'title': item.book.title,
            'price': item.book.rent_price,
            'return_date': timezone.now().date() + timedelta(days=14)
        })
    cart_items.delete()

    return Response({
        'message': 'Books checked out successfully.',
        'bill': bill,
        'total': total,
        'return_by': timezone.now().date() + timedelta(days=14)
    })



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def save_for_later(request):
    book_id = request.data.get('book_id')
    book = get_object_or_404(Book, id=book_id)
    request.user.profile.saved_books.add(book)
    return Response({'message': 'Book saved for later'}, status=200)

