from students.models import Student
from classes.models import Class

from base.base_admin_permissions import BaseAdminUsersAd
from base.constants import CURRENT_YEAR

class IndexAdminitrationView(BaseAdminUsersAd, TemplateView):
    template_name = 'administration/index-administration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.filter(classroom__year=CURRENT_YEAR)
        context['classes'] = Class.objects.filter(year=CURRENT_YEAR)
        return context

class AdministrationSearchView(BaseAdminUsersAd, ListView):

    model = Student

    template_name = 'administration/index-administration.html'

    def get_queryset(self):
        qs = super().get_queryset()
        term = self.request.GET.get('term')

        if term:
            qs = qs.filter(
                Q(student_name__istartwith= term)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classes = Class.objects.all().filter(
            class_school_year__year_school_stage__basic_stage_year__year_lective_year=CURRENT_YEAR
        )

        context['classes'] = classes

        return context




