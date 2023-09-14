from django import forms 

class PlaceForm(forms.Form):
    place = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Enter Your Location',
                                                                          'name': 'city',
                                                                          }))

