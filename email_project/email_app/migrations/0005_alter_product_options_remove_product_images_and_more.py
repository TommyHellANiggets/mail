# Generated by Django 5.1 on 2024-08-24 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0004_alter_color_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(choices=[('red', 'Красный'), ('blue', 'Синий'), ('green', 'Зелёный'), ('yellow', 'Жёлтый'), ('black', 'Чёрный'), ('white', 'Белый'), ('pink', 'Розовый'), ('purple', 'Фиолетовый'), ('orange', 'Оранжевый'), ('grey', 'Серый')], max_length=20, unique=True, verbose_name='Цвет'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='email_app.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
