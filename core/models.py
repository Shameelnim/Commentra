from django.db import models

class Comment(models.Model):
	img = models.ImageField(upload_to='images',null=True)
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	