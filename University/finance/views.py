from django.shortcuts import render
from django. views.generic.base import TemplateView

class IndexFinanceView(TemplateView):
    template_name = 'finance/index_finance.html'
