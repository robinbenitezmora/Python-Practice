from django.shortcuts import redirect, render,reverse
from django.db.models import Case, CharField, Value, When

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django.db.models import Q

from students.models import Student
from classes.models import Class
from base.base_admin_permissions import BaseAdminUsersSe
from base.constants import CURRENT_YEAR

class IndexSecretaryView(BaseAdminUsersSe, ListView):
    template_name = 'secretary/index_secretary.html'

class SecretarySearchView(BaseAdminUsersSe, TemplateView):
    model = Student
    template_name = 'secretary/search_se.html'

    def get_queryset(self):
        qs = super().get_queryset()
        term = self.request.GET.get('term')

        if term:
            qs = qs.filter(
                Q(student_name__istartswith=term)
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        classes = Class.objects.filter(
            class_lective_year = CURRENT_YEAR
        ).annotate(
            scholar_year_display=Case(
                When(school_year_class='CR', then=Value('Creche')),
				When(school_year_class='G1', then=Value('Kindergarten I')),
				When(school_year_class='G2', then=Value('Kindergarten II')),
				When(school_year_class='G3', then=Value('Kindergarten III')),
				When(school_year_class='G4', then=Value('Garden I')),
				When(school_year_class='G5', then=Value('Garden II')),
				When(school_year_class='1A', then=Value('1º Year')),
				When(school_year_class='2A', then=Value('2º Year')),
				When(school_year_class='3A', then=Value('3º Year')),
				When(school_year_class='4A', then=Value('4º Year')),
				When(school_year_class='5A', then=Value('5º Year')),
				When(school_year_class='6A', then=Value('6º Year')),
				When(school_year_class='7A', then=Value('7º Year')),
				When(school_year_class='8A', then=Value('8º Year')),
				When(school_year_class='9A', then=Value('9º Year')),
				output_field=CharField()
            )
        ).values_list(
            'year_school_display',
			'class_name',
			'class_basic_stage',
			'class_student'
        )

        context['classes'] = classes

        return context



