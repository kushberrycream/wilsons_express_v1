from django.contrib import admin
from .models import Create_account


class Create_accountAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'company_name',
        'freight',
        'date',
        'complete',
    )

    ordering = ('-date',)


admin.site.register(Create_account, Create_accountAdmin)
