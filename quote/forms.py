from django import forms
from .models import Quote
from localflavor.gb.forms import GBPostcodeField


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = '__all__'

    delivery = GBPostcodeField(max_length=8)
    collection = GBPostcodeField(max_length=8)
