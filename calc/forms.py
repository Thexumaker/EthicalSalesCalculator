from django import forms
from calc.models import Order

class OrderForm(forms.ModelForm):

    CLOTHING_CHOICE= [
    ("T-Shirts/Long-Sleeves Total", "T-Shirts/Long-Sleeves Total"),
    ("Hoodies/Crewnecks Total", "Hoodies/Crewnecks Total"),
    ("Zipped Hoodies/Jackets/Windbreakers", "Zipped Hoodies/Jackets/Windbreakers"),
    ("Printing on Sleeves/Pocket", "Printing on Sleeves/Pocket"),
    ("Pants", "Pants")
    ]
    numLocations = forms.IntegerField()
    nonWhiteApparel = forms.BooleanField(initial=True, required=False)
    colorsF = forms.IntegerField()
    colorsB = forms.IntegerField()
    colorsR = forms.IntegerField()
    colorsL = forms.IntegerField()
    colorsSP = forms.IntegerField()
    colorsOS = forms.IntegerField()
    costPerItem = forms.IntegerField()
    margin = forms.FloatField()
    quantity = forms.IntegerField()
    clothingItem = forms.CharField(label='Which item of clothing', widget=forms.Select(choices=CLOTHING_CHOICE))
    class Meta:
        model = Order
        fields = ('numLocations', 'nonWhiteApparel', 'colorsF', 'colorsB', 'colorsR', 'colorsL', 'colorsSP', 'colorsOS', 'costPerItem','margin', 'quantity','clothingItem')
