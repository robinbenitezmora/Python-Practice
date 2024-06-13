from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import TeacherListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from unidecode import unidecode 

from teachers.models import Teacher
from teachers.forms import TeacherForm
from accounts.models import CustomUser
from base.base_admin_permissions import BaseAdminUsersAdSe, BaseAdminUsersPr

class TeacherListView(BaseAdminUsersAdSe, TeacherListView):
    template_name = 'teachers/index_teacher.html'

class TeacherNewView(BaseAdminUsersAdSe, CreateView):
    template_name = 'teachers/teacher_new.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teacher_new')
    success_message = 'Teacher successfully registered'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            cpf = request.POST.get('teacher_cpf')

            if cpf:
                cpf_split_1 = cpf.split('.')
                cpf_split_2 = ''.join(cpf_split_1).split('-')
                cpf_join = ''.join(cpf_split_2)
                username_teacher = f'pr{cpf_join}'

                cpf_qs = CustomUser.objects.filter(username=username_teacher)

                if not cpf_qs:
                    name_form = request.POST.get('teacher_name')
                    name_split = name_form.split(' ')
                    first_name = name_split[0]

                    if len(name_split) > 1:
                        last_name = name_split[-1]
                    else:
                        last_name = 'no last name'

                    password = f'{unidecode(first_name).lower()}{cpf_join[0:6]}'

                    CustomUser.objects.create_user(
                        username=username_teacher,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        department='pr',
                    )

            return self.form_valid(form)

        else:
            context = {'form': form}
            return render(request, self.template_name, context)

class TeacherUpdateView(BaseAdminUsersAdSe, UpdateView):
    template_name = 'teachers/teacher_change.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('teachers')
    success_message = 'Teacher successfully updated'

    def get_success_url(self):
        '''
        Redirect to the form of created 'teacher', (change view)
        '''

        return reverse('change_teacher', kwargs={'pk': self.object.pk})

class TeacherDeleteView(BaseAdminUsersAdSe, DeleteView):
    template_name = 'teachers/teacher_delete.html'
    model = Teacher
    success_url = reverse_lazy('teachers')
    success_message = 'Teacher successfully deleted'

    def get_success_url(self):
        '''
        Only necessary for display success message after delete
        '''
        messages.success(self.request, self.success_message)
        return reverse('teachers')

class TeacherListView(BaseAdminUsersAdSe, ListView):
    template_name = 'teachers/teacher.html'
    model = Teacher

