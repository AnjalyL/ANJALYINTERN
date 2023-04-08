from django.contrib import admin

# Register your models here.
from .models import Listing,booked

admin.site.register(Listing)
admin.site.register(booked)