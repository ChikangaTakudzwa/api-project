# Generated by Django 4.1.5 on 2023-02-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_category_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]