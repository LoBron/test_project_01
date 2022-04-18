# Generated by Django 4.0.1 on 2022-04-12 10:38

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atributcategory',
            options={'verbose_name': 'Атрибут', 'verbose_name_plural': 'Атрибуты'},
        ),
        migrations.AlterModelOptions(
            name='atributvalue',
            options={'verbose_name': 'Значение атрибута', 'verbose_name_plural': 'Значения атрибутов'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='atributcategory',
            name='slug',
            field=models.SlugField(default='null', max_length=100, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atributcategory',
            name='category',
            field=mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория'),
        ),
    ]