from django.db import models
from Authentication.models import Hospital

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

class BloodBankStock(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete = models.CASCADE)
    blood_group = models.CharField(max_length = 120, choices = BLOOD_GROUP)
    units_of_blood = models.IntegerField(default = 0)
    latitude = models.CharField(max_length = 20, default = "0")
    longitude = models.CharField(max_length = 20, default = "0")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.hospital.name