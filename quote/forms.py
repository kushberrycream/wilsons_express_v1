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
          'length', 'width', 'service', 'spec_service', 'height1',
          'weight1', 'length1', 'width1', 'width2', 'height2', 'weight2',
          'length2', 'width3', 'height3', 'weight3', 'length3', 'width4',
          'height4', 'weight4', 'length4', 'email', 'phone_number',
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
            'height': 'Height', 'length': 'Length',
            'width': 'Width', 'weight': 'Weight',
            'service': 'Service', 'spec_service': 'Special',
            'height1': 'Height', 'length1': 'Length',
            'width1': 'Width', 'weight1': 'Weight',
            'height2': 'Height', 'length2': 'Length',
            'width2': 'Width', 'weight2': 'Weight',
            'height3': 'Height', 'length3': 'Length',
            'width3': 'Width', 'weight3': 'Weight',
            'height4': 'Height', 'length4': 'Length',
            'width4': 'Width', 'weight4': 'Weight',
            'email': 'Email Address', 'phone_number': 'Phone Number',
        }

        self.fields['c_postcode'].widget.attrs['autofocus'] = True
        self.helper = FormHelper(self)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
