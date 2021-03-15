from django.contrib import admin
from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    class Media:
        css = {
          'all': ('static/quote/css/quote_admin.css',),
        }
    search_fields = (
      "quote_ref__startswith", "c_postcode__startswith",
      "d_postcode__startswith"
    )

    readonly_fields = (
      'quote_ref', 'date', 'c_postcode', 'd_postcode', 'overall_weight',
      'overall_volume', 'height', 'length', 'width', 'weight', 'volume_weight',
      'pound_amount', 'height1', 'width1', 'length1', 'weight1',
      'volume_weight1', 'height2', 'width2', 'length2', 'weight2',
      'volume_weight2', 'height3', 'width3', 'length3', 'weight3',
      'volume_weight3', 'height4', 'width4', 'length4', 'weight4',
      'volume_weight4',
      )

    list_display = (
      'quote_ref', 'c_postcode', 'd_postcode', 'date', 'overall_weight',
      'overall_volume', 'pound_amount'
      )

    fieldsets = (
        (None, {
            'fields': (
              'quote_ref', 'date', 'c_postcode', 'd_postcode', 'pound_amount',
              'overall_weight', 'overall_volume',)
        }),
        ('Item 1', {
            'fields': ((
              'height', 'width', 'length', 'weight', 'volume_weight'),),
            'classes': ('required', 'thinner_labels', ),
        }),
        ('Item 2', {
            'fields': ((
              'height1', 'width1', 'length1', 'weight1', 'volume_weight1'),),
            'classes': ('required',),
        }),
        ('Item 3', {
            'fields': ((
              'height2', 'width2', 'length2', 'weight2', 'volume_weight2'),),
            'classes': ('required',),
        }),
        ('Item 4', {
            'fields': ((
              'height3', 'width3', 'length3', 'weight3', 'volume_weight3'),),
            'classes': ('required',),
        }),
        ('Item 5', {
            'fields': ((
              'height4', 'width4', 'length4', 'weight4', 'volume_weight4'),),
            'classes': ('required',),
        }),
        

    )


admin.site.register(Quote, QuoteAdmin)
admin.site.site_header = "Wilson's Express Admin"
admin.site.site_title = "Wilson's Express Admin"
admin.site.index_title = "Wilson's Express administration"
admin.empty_value_display = '**Empty**'
