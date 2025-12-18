from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect


def index(request):
    return render(request, 'home.html')


def latest(request):
    return render(request, 'latest.html')


def projects(request):
    return render(request, 'Projects.html')


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'thank_you.html', {'name': name, 'email': email})
    return render(request, 'contact.html')
