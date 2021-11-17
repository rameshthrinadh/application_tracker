from django.contrib import admin
from .models import applications,admins

# Register your models here.
admin.site.register(applications)
admin.site.register(admins)