# Generated by Django 4.1.7 on 2023-03-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livrariaapp', '0002_livros_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='livrariaapp/'),
        ),
    ]