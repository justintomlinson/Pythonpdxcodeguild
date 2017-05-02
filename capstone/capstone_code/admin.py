from django.contrib import admin
from capstone_code.models import Wine

# Register your models here.

class WineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wine, WineAdmin)
