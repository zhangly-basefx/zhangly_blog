from django.contrib import admin
from .models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display=("owner","content","link")

admin.site.register(Information,InformationAdmin)

