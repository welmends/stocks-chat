from django import forms
from django.forms import ModelForm
from .models import Room

class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(CreateRoomForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False

    def clean_name(self):
        special_characters = '!@#$%^&*()-+?=,_<>/'
        name = self.cleaned_data.get('name')
        if any(sc in name for sc in special_characters):
            raise forms.ValidationError('Room name must not contains special characters: {}'.format(special_characters))
        return name