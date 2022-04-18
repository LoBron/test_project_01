# Generated by Django 4.0.1 on 2022-04-19 08:12

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtributCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название атрибута')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Атрибут',
                'verbose_name_plural': 'Атрибуты',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('main_photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Главная фотография')),
                ('additional_photo_01', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Доп фото 1')),
                ('additional_photo_02', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Доп фото 2')),
                ('additional_photo_03', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Доп фото 3')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='AtributValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Значение атрибута')),
                ('atribut_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.atributcategory', verbose_name='Атрибут категории')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Значение атрибута',
                'verbose_name_plural': 'Значения атрибутов',
            },
        ),
        migrations.AddField(
            model_name='atributcategory',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='Категория'),
        ),
    ]
