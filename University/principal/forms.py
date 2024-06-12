from django import forms

from principal.models import Discipline

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = [
            'discipline_name',
            'discipline_teacher',
        ]