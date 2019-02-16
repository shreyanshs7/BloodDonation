from django.contrib import admin
from BloodBank.models import BloodBankStock

# Register your models here.
class BloodBankStockAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'blood_group', 'units_of_blood']
admin.site.register(BloodBankStock, BloodBankStockAdmin)