from django import forms

from principal.models import (
    LectiveYear,
    BasicStage,
    SchoolYear
)

class LectiveYearForm(forms.ModelForm):
    class Meta:
        model = LectiveYear
        fields = [
            'lective_year_name'
        ]

class BasicStageForm(forms.ModelForm):
    class Meta:
        model = BasicStage
        fields = [
            'basic_stage_name',
            'basic_stage_year',
        ]

class SchoolYearForm(forms.ModelForm):
    class Meta:
        model = SchoolYear
        fields = [
            'school_year_name',
            'school_year_stage',
        ]