from django.shortcuts import render


def index_secretary_view(request):
    return render(request, 'secretary/index_secretary.html')