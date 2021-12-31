from django.db import models

# Create your models here.


class UserForm(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	phno = models.CharField(max_length=14)
	msg = models.CharField(max_length=500)

	class Meta:
		app_label = 'formdata'

	def __str__(self) -> str:
		return self.name

	