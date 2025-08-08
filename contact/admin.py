from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('code', 'first_name', 'last_name', 'email', 'phone_number', 'created_at')
    search_fields = ('code', 'first_name', 'last_name', 'email')
    #list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('first_name', 'last_name')
    list_per_page = 20
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('code', 'created_at'),
        }),
    )
