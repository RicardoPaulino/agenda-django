from django.contrib import admin
from .models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'created_at','category', 'show')
    search_fields = ('code', 'first_name', 'last_name', 'email')
    #list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('first_name', 'last_name')
    list_editable = ['show']
    list_per_page = 20
    # fieldsets = (
    #     (None, {
    #         'fields': ('first_name', 'last_name', 'email', 'phone_number', 'description','category')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('code', 'created_at','show', 'picture'),
    #     }),
    # )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')
    search_fields = ('code', 'name')
    list_per_page = 20