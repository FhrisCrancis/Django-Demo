from django.contrib import admin
from .models import Member

# Register your models here.

#table name, not app name
admin.site.register(Member)
