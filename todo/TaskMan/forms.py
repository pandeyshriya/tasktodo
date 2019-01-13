from django import forms
from .models import todo

class ListForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ["Task", "completed", "Deadline"]