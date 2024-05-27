from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from students.models import Student
from students.forms import StudentForm

class StudentIndexView(TemplateView):
    template_name = 'students/index_student.html'

@method_decorator(login_required, name='dispatch')
class StudentNewView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/new_student.html'
    success_url = '/students/new_student'
    success_message = 'Student created successfully'

    def get(self, request, *args, **kwargs):

        context = {
            'form': StudentForm(),
            'student_obj': Student.objects.all()
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)

        if form.is_valid():
            form_model = form.save(commit=False)
            form_model.save()
            form.save_m2m()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        else:
            messages.error(request, 'Confirm the form fields')
            context = {
                'form': StudentForm(request.POST),
                'student_obj': Student.objects.all()
            }
            return render(request, self.template_name, context)
