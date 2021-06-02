from django import forms
from .models import Quote, Bookings
from localflavor.gb.forms import GBPostcodeField, GBCountySelect
from crispy_forms.helper import FormHelper


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = {
          'c_postcode', 'd_postcode', 'height', 'weight',
          'length', 'width', 'service', 'spec_service', 'height1',
          'weight1', 'length1', 'width1', 'width2', 'height2', 'weight2',
          'length2', 'width3', 'height3', 'weight3', 'length3', 'width4',
          'height4', 'weight4', 'length4', 'bookers_email',
          'bookers_phone_number',
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
            'bookers_email': 'Email Address',
            'bookers_phone_number': 'Phone Number (Use Country Code eg. +44)',
            'c_contact_name': 'Contact Name',
            'c_company': 'Company Name',
            'c_email': 'Email',
            'c_phone_number': 'Phone No.',
            'c_street_address1': 'Address Line 1',
            'c_street_address2': 'Address Line 2',
            'c_town_or_city': 'Town Or City',
            'c_county': 'County',
            'd_contact_name': 'Contact Name',
            'd_company': 'Company Name',
            'd_email': 'Email',
            'd_phone_number': 'Phone No.',
            'd_street_address1': 'Address Line 1',
            'd_street_address2': 'Address Line 2',
            'd_town_or_city': 'Town or City',
            'd_county': 'County',
        }

        self.fields['c_postcode'].widget.attrs['autofocus'] = True
        self.helper = FormHelper(self)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder


class BookingForm(QuoteForm):

    class Meta:
        model = Bookings
        fields = {
          'c_postcode', 'd_postcode', 'height', 'weight',
          'length', 'width', 'service', 'spec_service', 'height1',
          'weight1', 'length1', 'width1', 'width2', 'height2', 'weight2',
          'length2', 'width3', 'height3', 'weight3', 'length3', 'width4',
          'height4', 'weight4', 'length4', 'bookers_email', 'c_company',
          'bookers_phone_number', 'c_contact_name', 'c_email', 'c_county',
          'c_phone_number', 'c_street_address1', 'c_street_address2',
          'c_town_or_city', 'd_company', 'd_contact_name', 'd_email',
          'd_county', 'd_phone_number', 'd_street_address1',
          'd_street_address2', 'd_town_or_city',

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
    c_county = forms.CharField(widget=GBCountySelect())
    d_county = forms.CharField(widget=GBCountySelect())
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
        super(BookingForm, self).__init__(*args, **kwargs)
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
            'bookers_email': 'Email Address',
            'bookers_phone_number': 'Phone Number (Use Country Code eg. +44)',
            'c_contact_name': 'Contact Name',
            'c_company': 'Company Name',
            'c_email': 'Email',
            'c_phone_number': 'Phone No.',
            'c_street_address1': 'Address Line 1',
            'c_street_address2': 'Address Line 2',
            'c_town_or_city': 'Town Or City',
            'c_county': 'County',
            'd_contact_name': 'Contact Name',
            'd_company': 'Company Name',
            'd_email': 'Email',
            'd_phone_number': 'Phone No.',
            'd_street_address1': 'Address Line 1',
            'd_street_address2': 'Address Line 2',
            'd_town_or_city': 'Town or City',
            'd_county': 'County',
        }
        self.fields['height'].widget.attrs['readonly'] = True
        self.fields['height1'].widget.attrs['readonly'] = True
        self.fields['height2'].widget.attrs['readonly'] = True
        self.fields['height3'].widget.attrs['readonly'] = True
        self.fields['height4'].widget.attrs['readonly'] = True
        self.fields['width'].widget.attrs['readonly'] = True
        self.fields['width1'].widget.attrs['readonly'] = True
        self.fields['width2'].widget.attrs['readonly'] = True
        self.fields['width3'].widget.attrs['readonly'] = True
        self.fields['width4'].widget.attrs['readonly'] = True
        self.fields['weight'].widget.attrs['readonly'] = True
        self.fields['weight1'].widget.attrs['readonly'] = True
        self.fields['weight2'].widget.attrs['readonly'] = True
        self.fields['weight3'].widget.attrs['readonly'] = True
        self.fields['weight4'].widget.attrs['readonly'] = True
        self.fields['length'].widget.attrs['readonly'] = True
        self.fields['length1'].widget.attrs['readonly'] = True
        self.fields['length2'].widget.attrs['readonly'] = True
        self.fields['length3'].widget.attrs['readonly'] = True
        self.fields['length4'].widget.attrs['readonly'] = True
        self.fields['c_contact_name'].widget.attrs['autofocus'] = True
        self.helper = FormHelper(self)
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholder
