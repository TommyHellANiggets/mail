# Generated by Django 5.1 on 2024-08-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0005_alter_product_options_remove_product_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ozon_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Ozon'),
        ),
        migrations.AddField(
            model_name='product',
            name='wildberries_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Wildberries'),
        ),
    ]
