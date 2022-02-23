# Generated by Django 4.0.1 on 2022-02-22 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name_product',
            field=models.CharField(default='null', max_length=50, verbose_name='Название товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='photos',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.photo', verbose_name='Фотографии'),
        ),
    ]