from .models import Exercise
from django import forms


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'sets', 'reps', 'weight',)