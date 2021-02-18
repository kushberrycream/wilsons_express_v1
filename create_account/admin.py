from django.contrib import admin
from .models import Create_account


class Create_accountAdmin(admin.ModelAdmin):

    list_display_links = ('full_name', 'company_name')
    list_filter = ('freight',)
    list_display = (
        'full_name',
        'company_name',
        'freight',
        'date',
        'complete',
    )
    fields = (
        'full_name',
        'company_name',
        'phone_number',
        'email',
        'street_address1',
        'street_address2',
        'town_or_city',
        'postcode',
        'country',
        'freight',
        'date',
        'other_comments',
        'complete',
    )
    readonly_fields = (
        'full_name',
        'company_name',
        'phone_number',
        'email',
        'street_address1',
        'street_address2',
        'town_or_city',
        'postcode',
        'country',
        'freight',
        'date',
        'other_comments',
    )

    ordering = ('-date', 'company_name')
    search_fields = ('full_name', 'company_name', 'freight', )

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Create_account, Create_accountAdmin)
