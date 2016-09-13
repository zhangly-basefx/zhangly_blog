from django.contrib import admin
from .models import Activate

class ActivateAdmin(admin.ModelAdmin):
    list_display = ("user","activate_code")



admin.site.register(Activate,ActivateAdmin)
