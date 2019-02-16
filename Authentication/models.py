from django.db import models
from django.contrib.auth.models import User
# Create your models here.

O_POSITIVE = 'O+'
O_NEGATIVE = 'O-'
A_POSITIVE = 'A+'
A_NEGATIVE = 'A-'
B_POSITIVE = 'B+'
B_NEGATIVE = 'B-'
AB_POSITIVE = 'AB+'
AB_NEGATIVE = 'AB-'
BLOOD_GROUP = (
    (O_POSITIVE, "O+"),
    (O_NEGATIVE, "O-"),
    (A_POSITIVE, "A+"),
    (A_NEGATIVE, "A-"),
    (B_POSITIVE, "B+"),
    (B_NEGATIVE, "B-"),
    (AB_POSITIVE, "AB+"),
    (AB_NEGATIVE, "AB-"),
)

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
	blood_group = models.CharField(max_length = 10, choices = BLOOD_GROUP, default = "A+")
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
	latitude = models.CharField(max_length = 20, default = "0")
	longitude = models.CharField(max_length = 20, default = "0")
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name
