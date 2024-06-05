from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'webpage/index.html'

class IndexManagerView(TemplateView):

    def get(self, request, *args, **kwargs):
        '''
        After user login, redirect for respective dashboard,
        depending on the department
        '''

        department = {
            'AD': 'administration',
            'SE': 'secretary',
            'PR': 'professor',
            'ST': 'student',
            'FI': 'financer',
            'TE': 'teacher',
            'PA': 'parens',
        }

        if request.user.is_authenticated:

            template = department[request.user.department]
            return redirect('index_{}'.format(template))

        else:
            return render((request, 'webpage/index.html'))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                     