from django.db import models


# Create your models here.
class BaseModel(models.Model):
    id_delete = models.BooleanField(default=False)
    create_time = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        # 在元数据中声明当前表为抽象表
        abstract = True


class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish = models.CharField(max_length=128)
    address = models.CharField(max_length=256)

    # @property
    # def id(self):
    #     return self.id

    class Meta:
        db_table = 't_book'
        verbose_name = '图书表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name
