from django.forms import ModelForm, fields

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "content",)