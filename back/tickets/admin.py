from django.contrib import admin

from .models import Tags, Tickets, TelegramUsers, Statuses


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class StatusesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'telegram_id',
        'first_name',
        'second_name',
    )
    search_fields = (
        'first_name',
        'second_name',
    )
    empty_value_display = '-пусто-'


class TicketsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'status',
        'tag',
    )
    search_fields = (
        'title',
        'description',
    )
    empty_value_display = '-пусто-'


admin.site.register(Tags, TagsAdmin)
admin.site.register(Statuses, StatusesAdmin)
admin.site.register(TelegramUsers, TelegramUsersAdmin)
admin.site.register(Tickets, TicketsAdmin)

