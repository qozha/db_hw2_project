from django.contrib import admin
from apis.models import Discover, Disease, Country

# Register your models here.

admin.site.register(Disease)
admin.site.register(Country)
admin.site.register(Discover)