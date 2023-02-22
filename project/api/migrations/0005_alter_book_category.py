# Generated by Django 4.1.5 on 2023-02-22 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_category_slug_alter_book_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.category"
            ),
        ),
    ]
