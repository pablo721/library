# Generated by Django 3.2.9 on 2021-11-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=32, verbose_name='title'),
        ),
    ]
