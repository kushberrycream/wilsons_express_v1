from django import forms
from .models import Quote
from django.utils.translation import ugettext_lazy as _
from localflavor.gb.forms import GBPostcodeField, GBCountySelect
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = {
          'c_postcode', 'd_postcode', 'height', 'weight',
          'length', 'width', 'service', 'spec_service'
        } 

    YEARS = ('2021', )
    SERVICE = (
      ('10am', '10am'),
      ('12am', '12am'),
      ('NextDay', 'NextDay'),
    )
    SPEC_SERVICE = (
      ('Fragile', 'Fragile'),
      ('Security', 'Security'),
      ('Liquid', 'Liquid'),
      ('Live Fish', 'Live Fish'),
      )
    d_postcode = GBPostcodeField(max_length=8)
    c_postcode = GBPostcodeField(max_length=8)
    service = forms.ChoiceField(
            widget=forms.CheckboxSelectMultiple(),
            choices=SERVICE,
            )
    spec_service = forms.ChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple(),
            choices=SPEC_SERVICE,
            )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
          
            'c_postcode': 'Collection Postcode',
            'd_postcode': 'Delivery Postcode',
            'height': 'Height',
            'length': 'Length',
            'width': 'Width',
            'weight': 'Weight',
            'service': 'Service',
            'spec_service': 'Special',
        }

        self.fields['c_postcode'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

        self.helper = FormHelper(self)
