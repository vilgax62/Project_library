from django.contrib import admin
from .models import Book, Reader ,IssuedBook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'rent_price')
    search_fields = ('title', 'author', 'isbn')
    # list_filter = ('issue_date', 'due_date')

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'library_card_number')
    search_fields = ('user__username', 'library_card_number')
    

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('user','book','issue_date','return_date','price')
    search_fields =('user','book')
    

# Custom admin site titles
admin.site.site_header = "Library Admin"
admin.site.site_title = " Admin Portal"
admin.site.index_title = "Welcome to  Library Management"








# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'isbn']
#     search_fields = ['title', 'author']

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'enrollment_number']