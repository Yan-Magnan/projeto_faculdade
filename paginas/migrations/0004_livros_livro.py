# Generated by Django 2.2.3 on 2021-11-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_livros_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='livro',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]