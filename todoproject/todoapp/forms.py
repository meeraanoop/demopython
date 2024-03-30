from datetime import datetime

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['date_due'].widget.attrs['value'] = datetime.today().strftime('%Y-%m-%d')
