from django.db import models

# Create your models here.
class link(models.Model):
	server_list_id=models.PositiveIntegerField()
	server_name=models.CharField(max_length=15)
	link=models.TextField()
	upvote=models.PositiveIntegerField()
	views=models.PositiveIntegerField()
