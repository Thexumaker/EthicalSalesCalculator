from django import forms
from calc.models import Order

class OrderForm(forms.ModelForm):
    numLocations = forms.IntegerField()
    nonWhiteApparel = forms.BooleanField()
    colorsF = forms.IntegerField()
    colorsB = forms.IntegerField()
    colorsR = forms.IntegerField()
    colorsL = forms.IntegerField()
    colorsSP = forms.IntegerField()
    colorsOS = forms.IntegerField()
    costPerItem = forms.IntegerField()
    margin = forms.FloatField()
    quantity = forms.IntegerField()
    class Meta:
        model = Order
        fields = ('numLocations', 'nonWhiteApparel', 'colorsF', 'colorsB', 'colorsR', 'colorsL', 'colorsSP', 'colorsOS', 'costPerItem','margin', 'quantity')
