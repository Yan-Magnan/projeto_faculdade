from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    def __str__(self):
        return self.nome



class Livros(models.Model):
    nome = models.CharField(max_length=80)
    editora = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    ano_Lancamento = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/')
    livro = models.FileField(blank=True, upload_to='pdfs/%y/%m/')
    # arquivo = models.FilePathField(blank=False)

    def __str__(self):
        return self.nome

class Livros2(models.Model):
    nome = models.CharField(max_length=80)
    editora = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    ano_Lancamento = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/')
    livro = models.FileField(blank=True, upload_to='pdfs/%y/%m/')
    # arquivo = models.FilePathField(blank=False)

    def __str__(self):
        return self.nome
class pet(models.Model):
    status = models.CharField(max_length=80)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/')
    nome = models.CharField(max_length=80)
    raca = models.CharField(max_length=80)
    tutor = models.CharField(max_length=180)
    email = models.CharField(max_length=260)
    telefone = models.CharField(max_length=80)
    cpf = models.CharField(max_length=260)
    endereco = models.CharField(max_length=150)
    data_acolhimento = models.DateTimeField(default=timezone.now)
    historico_medico = models.CharField(max_length=500000, blank=True)


    def __str__(self):
        return self.nome








