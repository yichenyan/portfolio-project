from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to='images/',null=True)
	summary = models.CharField(max_length=200,null=True)
	temp = models.CharField(max_length=200,null=True)


	def __str__(self):
		return self.summary