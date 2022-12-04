from django import forms
from .models import PDFName

class PDFNameForm(forms.ModelForm):
    class Meta:
        model=PDFName
        fields = ['pdfName']