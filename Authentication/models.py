from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetail(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female')
	)
	user  = models.ForeignKey(User, on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 120)
	last_name = models.CharField(max_length = 120)
	contact = models.CharField(max_length = 10)
	weight = models.IntegerField()
	gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)
	city = models.CharField(max_length = 120)
	state = models.CharField(max_length = 120)
	address = models.CharField(max_length = 200)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	@property
	def full_name(self):
		return ("%s %s")%(self.first_name, self.last_name)

	def __str__(self):
		return self.user.username

class Hospital(models.Model):
	username = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 120)
	state = models.CharField(max_length = 120)
	city = models.CharField(max_length = 120)
	address = models.CharField(max_length = 120)
	contact = models.CharField(max_length = 120)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name
