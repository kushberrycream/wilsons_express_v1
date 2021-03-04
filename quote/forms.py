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
        fields = '__all__'
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
    c_county = forms.CharField(label=_("County"), widget=GBCountySelect())
    d_county = forms.CharField(label=_("County"), widget=GBCountySelect())
    c_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    d_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    service = forms.ChoiceField(
            required=True,
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
            'fragile': 'fragile',
            'security': ' security',
            'service': 'Service',
            'spec_service': 'Special',
            'c_date': 'Collection Date',
            'd_date': 'Delivery Date',
            'd_contact_name': 'Contact Name',
            'd_company': 'Delivery Company Name',
            'd_email': 'Delivery Email',
            'd_phone_number': 'Delivery Phone No.',
            'd_street_address1': 'Delivery Address Line 1',
            'd_street_address2': 'Delivery Address Line 2',
            'd_town_or_city': 'Delivery Town or City',
            'd_county': 'Collection County',
            'c_contact_name': 'Contact Name',
            'c_company': 'Collecton Company Name',
            'c_email': 'Collection Email',
            'c_phone_number': 'Collection Phone No.',
            'c_street_address1': 'Collection Address Line 1',
            'c_street_address2': 'Collection Address Line 2',
            'c_town_or_city': 'Collection Town Or City',
            'c_county': 'Delivery County',
        }

        self.fields['d_contact_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

        self.fields['fragile'].label = 'Fragile'
        self.fields['security'].label = 'Security'
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
          InlineCheckboxes('service', ))
        self.helper.layout = Layout(
          InlineCheckboxes('spec_service', ))
