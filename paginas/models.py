from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=80)
    def __str__(self):
        return self.nome


class Pets(models.Model):
    STATUS_CHOICES = [
        ('Tutor não localizado', 'Tutor não localizado'),
        ('Tutor localizado', 'Tutor localizado'),
        ('Retirado pelo tutor', 'Retirado pelo tutor'),
    ]

    status = models.CharField(max_length=80, choices=STATUS_CHOICES, default='Status pendente')
    nome = models.CharField(max_length=80, default='Sem nome')
    raca = models.CharField(max_length=80, default='Raça pendente')
    tutor = models.CharField(max_length=180, default='Tutor pendente')
    email = models.CharField(max_length=260, default='Email pendente')
    telefone = models.CharField(max_length=80, default='Telefone pendente')
    cpf = models.CharField(max_length=260, default='xxx.xxx.xxx-xx')
    endereco = models.CharField(max_length=150, default='Sem endereço')
    data_acolhimento = models.DateTimeField(default=timezone.now)
    historico_medico = models.CharField(max_length=500000, blank=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/')
    # livro = models.FileField(blank=True, upload_to='pdfs/%y/%m/')
    # historico_medico = models.CharField(max_length=500000, blank=True)
    # arquivo = models.FilePathField(blank=False)

    def __str__(self):
        return self.nome
