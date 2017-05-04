from django.contrib import admin
from capstone_code.models import Wine, Winery, Cellar

# Register your models here.

class WineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wine, WineAdmin)

class WineryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Winery, WineryAdmin)

class CellarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cellar, CellarAdmin)



