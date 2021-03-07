from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):

    readonly_fields = (
      'quote_ref', 'date', 'c_postcode', 'd_postcode', 'height',
      'length', 'width', 'weight', 'volume_weight', 'quote'
      )
    fields = ('quote_ref', 'date', 'c_postcode', 'd_postcode',
              'height', 'length', 'width', 'weight', 'volume_weight', 'quote')

    list_display = ('quote_ref', 'c_postcode', 'd_postcode', 'date', 'quote')


admin.site.register(Quote, QuoteAdmin)
