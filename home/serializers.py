from rest_framework import serializers
from .models import Book , Cart ,SavedBook ,IssuedBook

class BookSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'rent_price', 'cover_image']

    def get_cover_image(self, obj):
        request = self.context.get('request')
        if obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url)
        return None
        
class CartSerializer(serializers.ModelSerializer):
    class meta:
        model= Cart
        field = '__all__'
        
class SavedBookSerializer(serializers.ModelSerializer):
    class meta:
        model= SavedBook
        field = '__all__'
        
        
class IssuedBookSerializer(serializers.ModelSerializer):
    class meta:
        model= IssuedBook
        field = '__all__'
        