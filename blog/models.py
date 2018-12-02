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

	#def __str__(self):
	#	return self.title
	def __str__(self):
		return self.title

	def text_short(self):
		max_text_to_display=60
		if len(self.text)>max_text_to_display:
			for i in range(max_text_to_display,0,-1):
				if self.text[i] == " ":
					return self.text[:i] + "......"
					break
		else:
			return self.text

	def time_created_friendly(self):
		return self.time_created.strftime('%b %e, %Y')

