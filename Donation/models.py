from django.db import models
from Authentication.models import UserDetail
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
	user = models.ForeignKey(UserDetail, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.user.user.username

class DonationRequest(models.Model):
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
	donation_request_by = models.ForeignKey(User, on_delete = models.CASCADE)
	blood_type = models.CharField(max_length = 120, choices = BLOOD_GROUP)
	units_of_blood = models.IntegerField()
	is_urgent = models.BooleanField(default = False)
	is_completed = models.BooleanField(default = False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.donation_request_by.username