from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','title', 'description','remark','priority', 'status']

class TaskFilterForm(forms.Form):
    PRIORITY_CHOICES = [
        ('', 'All'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False)


