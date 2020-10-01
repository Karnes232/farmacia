from django import forms
from .models import User

class CreateTitle(forms.Form):
    title = forms.CharField(label="Title")

class CreateDescription(forms.Form):
    description = forms.CharField(widget=forms.Textarea)

class CreateLink(forms.Form):
    photo_url = forms.URLField(required=True)


def SuperUser(current_user):
    superusers = User.objects.filter(is_superuser=True)
    current_id = User.objects.get(username=current_user)
    is_super = False
    for su in superusers:
        if current_id == su:
            is_super = True
    return is_super
    