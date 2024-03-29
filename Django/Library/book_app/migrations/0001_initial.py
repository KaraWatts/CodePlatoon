# Generated by Django 5.0.3 on 2024-03-27 21:22

import book_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[book_app.validators.validate_title_case])),
                ('author', models.CharField(max_length=50, validators=[book_app.validators.validate_title_case])),
                ('isbn', models.CharField(max_length=14, unique=True, validators=[book_app.validators.validate_isbn])),
                ('genre', models.CharField(max_length=50, validators=[book_app.validators.validate_title_case])),
                ('published_date', models.DateField()),
            ],
        ),
    ]
