from django.views.generic.base import TemplateView

class IndexTeacherView(TemplateView):
    template_name = 'teachers/index_teacher.html'
    
