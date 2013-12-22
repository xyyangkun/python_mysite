from django.db import models

class blog(models.Model):
	title = models.CharField(max_length=200)
	time = models.DateTimeField('date published')
	href = models.CharField(max_length=200)
	content = models.CharField(max_length=20000)

