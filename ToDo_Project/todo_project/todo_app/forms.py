from .models import todo_task
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_task
        fields = ['name','priority','date']

