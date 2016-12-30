from django import forms
from .models import POI


class POIForm(forms.ModelForm):

    class Meta:
        model = POI
        fields = ('name', 'pos_x', 'pos_y', 'special_icon')