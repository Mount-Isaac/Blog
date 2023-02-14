from django.db import models
from django.shortcuts import reverse
from datetime import datetime

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=1000000)
	create_date = models.DateTimeField(default=datetime.now, blank=True)


	def get_absolute_url(self):
		return reverse("blogging:read", kwargs={"id":self.id})