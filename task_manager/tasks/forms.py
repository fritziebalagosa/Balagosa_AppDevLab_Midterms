from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Ensure date picker
    is_completed = forms.BooleanField(required=False, label="Mark as Done")  # Checkbox

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_completed']  # Include checkbox
