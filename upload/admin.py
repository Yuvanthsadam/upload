from django.contrib import admin
from upload.models import profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','picture']
admin.site.register(profile, ProfileAdmin)