# Generated by Django 5.1.3 on 2024-11-28 07:26

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_api", "0004_alter_blog_title_alter_category_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog", old_name="image", new_name="blog_image",
        ),
        migrations.RenameField(
            model_name="blog", old_name="category", new_name="categories",
        ),
        migrations.AddField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="blog", name="title", field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="category", name="name", field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
