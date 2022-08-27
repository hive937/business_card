from django.shortcuts import render


def index(request):
    template = 'templates/index.html'
    return render(request, template)
