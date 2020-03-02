from django import forms
from docRecords.models import NewEntry

class NewEntryForm(forms.ModelForm):
    class Meta:
        model = NewEntry
        fields = '__all__'
        exclude = ['slug']