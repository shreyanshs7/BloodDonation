from django.contrib import admin
from Authentication.models import UserDetail, Hospital

# Register your models here.
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'contact', 'weight', 'gender', 'city', 'state']
admin.site.register(UserDetail, UserDetailAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'state', 'city', 'contact']
admin.site.register(Hospital, HospitalAdmin)