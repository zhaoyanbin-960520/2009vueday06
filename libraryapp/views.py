from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from libraryapp.models import Book
from libraryapp.serializer import BookModelSerializer, BookDeModelSerializer


class BookAPIView(APIView):
    def get(self, requset, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            # book_obj = Book.objects.filter(pk=id).values('id','book_name','price','create_time','publish','address').first()
            book_obj = Book.objects.filter(pk=id).first()
            data = BookModelSerializer(book_obj).data
            return Response(
                {"message": "查询单个成功",
                 "results": data}
            )
        else:
            # query_set = Book.objects.all().values('id','book_name','price','create_time','publish','address')
            query_set = Book.objects.all()
            data = BookModelSerializer(query_set, many=True).data
            return Response(
                {"message": "查询多个成功",
                 "results": data}
            )

    def post(self, request, *args, **kwargs):
        request_data = request.data
        # print(request_data)

        serializer = BookDeModelSerializer(data=request_data)
        if serializer.is_valid():
            book_obj = serializer.save()

            return Response({
                "message": "新增图书成功",
                "results": BookModelSerializer(book_obj).data,
            })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get("id")
        # print(book_id)
        if book_id:
            rst = Book.objects.get(pk=book_id)
            rst.delete()
            # print(123)
            return Response({
                "message": "删除成功",
                "result":BookModelSerializer(rst).data
            })
        return Response({"message": "删除失败或图书不存在"})

    def patch(self, request, *args, **kwargs):
        request_data = request.data
        # print(request_data)
        book_id = request.data.get("id")
        # print(book_id)

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "message": "修改的图书不存在"
            })

        serializer = BookModelSerializer(data=request_data, instance=book_obj, partial=True)
        # print(serializer)
        serializer.is_valid(raise_exception=True)

        book = serializer.save()
        # print(book)
        return Response({
            "message": "修改成功",
            "results": BookModelSerializer(book).data
        })
