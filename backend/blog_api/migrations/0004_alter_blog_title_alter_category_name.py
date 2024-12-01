# Generated by Django 5.1.2 on 2024-11-01 15:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_api", "0003_category_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(
                max_length=255,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=255,
                validators=[django.core.validators.MinLengthValidator(1)],
            ),
        ),
    ]