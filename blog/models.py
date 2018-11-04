from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=50,null=True)
	author = models.CharField(max_length=10,null=True)
	text = models.TextField(null=True)
	image = models.ImageField(upload_to='images/',null=True)
	time = models.DateTimeField(null=True)
	time_created = models.DateTimeField(auto_now_add=True)
	time_updated = models.DateTimeField(auto_now=True)
	is_visible = models.BooleanField()

	def __str__(self):
		return self.title
