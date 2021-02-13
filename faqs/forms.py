from django import forms
from .models import Faqs


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faqs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input rounded-0'
