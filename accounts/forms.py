from django.forms import ModelForm

from .models import ContactMe


class ContactForm(ModelForm):
    class Meta:
        model = ContactMe
        fields = ['full_name', 'email', 'message']