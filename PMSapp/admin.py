from django.contrib import admin

from PMSapp.models import Member, Patient, ImageModel, Payment

# Register your models here.
admin.site.register(Member)
admin.site.register(Patient)
admin.site.register(ImageModel)
admin.site.register(Payment)