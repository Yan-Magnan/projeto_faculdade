# Generated by Django 2.2.3 on 2021-10-31 12:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('editora', models.CharField(max_length=80)),
                ('descricao', models.TextField(blank=True)),
                ('ano_Lancamento', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paginas.Categoria')),
            ],
        ),
    ]
