from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]
    search_fields = [field.name for field in CustomUser._meta.fields]
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUserAdmin)
