from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Case, CharField, Value, When

from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from unidecode import unidecode  # normalize strings Csii

from students.models import Student
from students.forms import StudentForm
from classes.models import Class
from accounts.models import CustomUser, CustomerUser

from base.constants import CURRENT_YEAR
from base.base_admin_permissions import BaseAdminUsersAdSe

def create_user_after_registration(
    username, password, first_name, last_name, department
):
    '''
    This function creates a user after the student registration
    '''
    CustomerUser.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        department=department
    )

def data_processing_user_creation(cpf, name_form, department):
    '''
    This function processes the data for user creation
    '''
    cpf_split_1 = cpf.split('.')
    cpf_split_2 = ''.join(cpf_split_1).split('-')
    cpf_join = ''.join(cpf_split_2)
    name_split = name_form.split()
    first_name = name_split[0]
    last_name = name_split[-1]
    password = f'{unidecode(first_name).lower()}{cpf_join[0:6]}'

    cpf_qs = CustomerUser.objects.filter(username=cpf_join)

    if not cpf_qs:
        create_user_after_registration(
            cpf_join, password, first_name, last_name, department
        )

# ---- General Views ---- #
class StudentIndexView(TemplateView):
    template_name = 'students/index_student.html'

class StudentInfoView(BaseAdminUsersAdSe):
    pass

class StudentNewView(BaseAdminUsersAdSe, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/new_student.html'
    success_url = reverse_lazy('new_student')
    success_message = 'Student created successfully'

    def post(self, request, *args, **kwargs):
        '''
            This function processes the data for student creation
        '''

        form = self.get_form()

        if form.is_valid():
            cpfa = request.POST.get('student_cpf')
            cpf1 = request.POST.get('student_affiliation1_cpf')
            cpf2 = request.POST.get('student_affiliation2_cpf')

            if cpfa:
                name_a_form = request.POST.get('student_name')

                data_processing_user_creation(cpf, name_a_form, 'st')

            if cpf1:
                name1_form = request.POST.get('student_affiliation1_name')

                data_processing_user_creation(cpf1, name1_form, 're')

            if cpf2:
                name2_form = request.POST.get('student_affiliation2_name')

                data_processing_user_creation(cpf2, name2_form, 're')

            return self.form_valid(form)
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

class StudentUpdateView(BaseAdminUsersAdSe, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_change.html'
    success_message = 'Student updated successfully'

    def get_success_url(self):
        '''
            This function returns the success URL
        '''
        return reverse('student_change', kwargs={'pk': self.object.pk})

class StudentDeleteView(BaseAdminUsersAdSe, DeleteView):
    model = Student
    template_name = 'students/student_delete.html'
    success_message = 'Student deleted successfully'

    def get_success_url(self):
        '''
            Only necessary for display success message after delete
        '''
        message.success(self.request, self.success_message)
        return reverse('students')

# ---- Lists Views ---- #
class StudentListView(BaseAdminUsersAdSe, ListView):
    model = Student
    paginate_by = 20
    template_name = 'students/students.html'

    def get_context_data(self, **kwargs):
        '''
            This function returns the context data
        '''
        context = super().get_context_data(**kwargs)
        
        classes = Class.objects.filter(
            classes_lective_year=CURRENT_YEAR
        ).annotate(
            school_year_display=Case(
                When(class_year_school='CR', then=Value('Creche')),
				When(class_year_school='G1', then=Value('Kindergarten I')),
				When(class_year_school='G2', then=Value('Kindergarten II')),
				When(class_year_school='G3', then=Value('Kindergarten III')),
				When(class_year_school='G4', then=Value('Garden I')),
				When(class_year_school='G5', then=Value('Garden II')),
				When(class_year_school='1A', then=Value('1º year')),
				When(class_year_school='2A', then=Value('2º year')),
				When(class_year_school='3A', then=Value('3º year')),
				When(class_year_school='4A', then=Value('4º year')),
				When(class_year_school='5A', then=Value('5º year')),
				When(class_year_school='6A', then=Value('6º year')),
				When(class_year_school='7A', then=Value('7º year')),
				When(class_year_school='8A', then=Value('8º year')),
				When(class_year_school='9A', then=Value('9º year')),
				output_field=CharField()
            )
        )

        context['classes'] = classes
        return context

class StudentEfectiveView(BaseAdminUsersAdSe, ListView):
    model = Student
    template_name = 'students/efective_student.html'
