from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):

    readonly_fields = ('date',)
    fields = ('date',
              'c_contact_name',
              'c_company',
              'c_email',
              'c_phone_number',
              'c_street_address1',
              'c_street_address2',
              'c_town_or_city',
              'c_county',
              'c_postcode',
              'd_contact_name',
              'd_company',
              'd_email',
              'd_phone_number',
              'd_street_address1',
              'd_street_address2',
              'd_town_or_city',
              'd_county',
              'd_postcode',
              'height',
              'length',
              'width',
              'weight', )
    list_display = ('d_postcode', 'c_postcode', 'date')


admin.site.register(Quote, QuoteAdmin)
