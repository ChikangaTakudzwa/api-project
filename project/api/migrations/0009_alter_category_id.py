# Generated by Django 4.1.5 on 2023-02-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_remove_book_category_alter_category_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]