# Generated by Django 4.1.5 on 2023-02-27 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_category_about_alter_book_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category_id',
        ),
    ]
