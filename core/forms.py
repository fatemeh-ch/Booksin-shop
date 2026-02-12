from django import forms
from core.models import Contact

# Contact Form
class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields=['name','subject','email','message']