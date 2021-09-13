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
        name = self.cleaned_data.get('name')
        if name.isalpha()==False:
            raise forms.ValidationError('Room name must not contains special characters')
        return name