from django import forms
from . import models

class InputForm(forms.ModelForm):
    class Meta:
        model = models.InputModel
        fields = "__all__"
        labels = {
            "text_msg" : "Your message:"
        }