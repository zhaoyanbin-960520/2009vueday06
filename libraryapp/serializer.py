from rest_framework.serializers import ModelSerializer

from libraryapp.models import Book


class BookModelSerializer(ModelSerializer):
    class Meta:
        model=Book

        fields=['id','book_name','price','create_time','publish','address']

class BookDeModelSerializer(ModelSerializer):
    """反序列化：数据库入库时使用"""

    class Meta:
        model = Book
        fields = ('book_name','price','create_time','publish','address')