# Generated by Django 2.2.3 on 2021-11-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0006_auto_20211107_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeusLivros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.ManyToManyField(blank=True, null=True, to='paginas.Livros')),
            ],
        ),
        migrations.DeleteModel(
            name='Meus_Livros',
        ),
    ]
