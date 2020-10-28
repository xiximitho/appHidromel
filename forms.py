
from django import forms

class CalculoABVForm(forms.Form):
    og = forms.FloatField(label='Original Gravity')
    fg = forms.FloatField(label='Final Gravity')
