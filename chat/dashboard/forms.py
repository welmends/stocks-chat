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