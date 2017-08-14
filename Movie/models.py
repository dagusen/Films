from django.db import models

# Create your models here.

class Film(models.Model):
	Title = models.CharField(max_length=150)
	Description = models.TextField()
	Year = models.DateTimeField('Date Published')

	def __str__(self):
		return self.Title
