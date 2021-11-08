from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	titulo = models.CharField(max_length=50)
	imagem = models.FileField(upload_to="%Y/%m/%d/")
	texto = models.CharField(max_length=50, default='nome científico')
	tamanho = models.CharField(max_length=50, default='tamanho da espécie')
	cores = models.CharField(max_length=50, default='cores da espécies')
	caract = models.CharField(max_length=300, default='características da espécie')
	sobre = models.CharField(max_length=300, default='sobre a espécie')
	SUCU = 'SC'
	FITO = 'FT'
	tipo_planta = [
		('-', '-'),
		(SUCU, 'Suculentas'),
		(FITO, 'Fitoterápicas'),
	]
	tipo = models.CharField(
		max_length = 2,
		choices = tipo_planta,
		default = '-',
	)
	data_criacao = models.DateField(auto_now=True)
	data_publicacao = models.DateTimeField(default=timezone.now)
	autor = models.ForeignKey(User, on_delete=models.PROTECT)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})

	def __str__(self):
		return self.titulo

class Sugestao(models.Model):
	sugestao = models.TextField()
	recado = models.TextField()
	categoria = models.CharField(max_length=50)
	foto = models.FileField()

