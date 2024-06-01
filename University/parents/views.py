from django.views.generic.base import TemplateView

class IndexParentView(TemplateView):
    template_name = 'parents/index_parent.html'