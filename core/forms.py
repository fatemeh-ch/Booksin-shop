from django import forms
from core.models import Contact
from captcha.fields import CaptchaField

# Contact Form
class ContactForm(forms.ModelForm):
    captcha=CaptchaField()

    class Meta:
        model=Contact
        fields=['name','subject','email','message']