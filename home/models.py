from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User

# 👇 Helper function must be declared first
def get_return_date():
    return timezone.now().date() + timedelta(days=14)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    rent_price = models.DecimalField(max_digits=6, decimal_places=1)
    # issue_date = models.DateField(null=True, blank=True)
    # due_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    issued_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library_card_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.user.username

# 👇 Changed to ForeignKey for simpler API handling
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Add this if 'book' field is causing migration issues (make it nullable temporarily)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    
    # Use this if 'added_at' is causing issues with auto_now_add and existing rows
    added_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"{self.user.username} added {self.book.title if self.book else 'No Book'}"


class SavedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.book.title}"

class IssuedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=get_return_date)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return f"{self.user.username} issued {self.book.title}"

