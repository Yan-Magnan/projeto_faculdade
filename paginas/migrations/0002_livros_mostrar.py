# Generated by Django 2.2.3 on 2021-10-31 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]