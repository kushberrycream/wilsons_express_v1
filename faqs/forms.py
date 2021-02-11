from django import forms
from .models import Faqs


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faqs
        fields = '__all__'
