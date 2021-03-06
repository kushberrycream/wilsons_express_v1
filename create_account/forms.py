from django import forms
from .models import Create_account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Create_account
        fields = (
          'full_name', 'company_name', 'phone_number', 'email',
          'street_address1', 'street_address2', 'town_or_city',
          'postcode', 'country', 'freight', 'other_comments',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'company_name': 'Company Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'freight': 'Freight ',
            'other_comments': 'Other Comments',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields['freight'].choices = [
                    ("", "Freight Type *"), ] + list(
                        self.fields['freight'].choices)[1:]
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
