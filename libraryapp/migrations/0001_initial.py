# Generated by Django 2.0.6 on 2021-01-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_delete', models.BooleanField(default=False)),
                ('create_time', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('book_name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('publish', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': '图书表',
                'verbose_name_plural': '图书表',
                'db_table': 't_book',
            },
        ),
    ]
