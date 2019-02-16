from django.contrib import admin
from Donation.models import Donor, DonationRequest

# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    list_display = ['__str__']
admin.site.register(Donor, DonorAdmin)

class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'blood_type', 'units_of_blood', 'is_urgent', 'is_completed']
admin.site.register(DonationRequest, DonationRequestAdmin)