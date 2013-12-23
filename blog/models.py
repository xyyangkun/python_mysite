from django.db import models

class blog(models.Model):
	title = models.CharField(max_length=200)
	time = models.DateTimeField('date published')
	href = models.CharField(max_length=200)
	content = models.TextField(max_length=20000)
	def __unicode__(self):
		return self.title
