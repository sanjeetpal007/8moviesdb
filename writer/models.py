from django.db import models

# Create your models here.
class writer(models.Model):
	writer_name=models.CharField(max_length=40)
	image_id=models.PositiveSmallIntegerField()
