from django.views.generic.base import TemplateView

class IndexAdminstrationView(TemplateView):
    template_name = 'administration/index-administration.html'
