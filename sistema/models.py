from django.db import models

class Selecao(models.Model):
	time1 = models.CharField(max_length=100)
	gols1 = models.CharField(max_length=100)
	time2 = models.CharField(max_length=100)
	gols2 = models.CharField(max_length=100)



