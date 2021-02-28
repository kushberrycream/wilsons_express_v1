from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):

    readonly_fields = ('date',)
    fields = ('delivery', 'collection', 'date')
    list_display = ('delivery', 'collection', 'date')


admin.site.register(Quote, QuoteAdmin)
