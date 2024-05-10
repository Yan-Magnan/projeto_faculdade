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

    RACA_CHOICES = [
        ('Labrador Retriever', 'Labrador Retriever'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Pastor Alemão', 'Pastor Alemão'),
        ('Bulldog Francês', 'Bulldog Francês'),
        ('Beagle', 'Beagle'),
        ('Poodle', 'Poodle'),
        ('Boxer', 'Boxer'),
        ('Yorkshire Terrier', 'Yorkshire Terrier'),
        ('Dachshund (Salsicha)', 'Dachshund (Salsicha)'),
        ('Bulldog Inglês', 'Bulldog Inglês'),
        ('Chihuahua', 'Chihuahua'),
        ('Shih Tzu', 'Shih Tzu'),
        ('Pug', 'Pug'),
        ('Border Collie', 'Border Collie'),
        ('Rottweiler', 'Rottweiler'),
        ('Caramelo', 'Caramelo'),
        ('Outra', 'Outra')
    ]
    raca = models.CharField(max_length=80, choices=RACA_CHOICES, default='Outra')

    ESPECIE_CHOICES = [
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Outra', 'Outra')
    ]
    especie = models.CharField(max_length=80, choices=ESPECIE_CHOICES, default='Outra')

    PORTE_CHOICES = [
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G')
    ]
    porte = models.CharField(max_length=80, choices=PORTE_CHOICES, default='Outra')

    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea')
    ]
    sexo = models.CharField(max_length=80, choices=SEXO_CHOICES, default='Outra')

    nome = models.CharField(max_length=80, default='Sem nome')
    local_resgate = models.CharField(max_length=500, default='Local não informado')
    tutor = models.CharField(max_length=180, default='Tutor pendente')
    email = models.CharField(max_length=260, default='Email pendente')
    telefone = models.CharField(max_length=80, default='Telefone pendente')
    cpf = models.CharField(max_length=260, default='xxx.xxx.xxx-xx')
    endereco = models.CharField(max_length=150, default='Sem endereço')
    data_acolhimento = models.DateTimeField(default=timezone.now)
    historico_medico = models.CharField(max_length=500000, blank=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%y/%m/')
    # arquivo = models.FilePathField(blank=False)

    def __str__(self):
        return self.nome



