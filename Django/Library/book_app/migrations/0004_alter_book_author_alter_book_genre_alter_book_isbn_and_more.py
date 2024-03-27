# Generated by Django 5.0.3 on 2024-03-27 22:42

import book_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_alter_book_author_alter_book_genre_alter_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, validators=[book_app.validators.validate_title_case]),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=50, validators=[book_app.validators.validate_title_case]),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=14, unique=True, validators=[book_app.validators.validate_isbn]),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, validators=[book_app.validators.validate_title_case]),
        ),
    ]