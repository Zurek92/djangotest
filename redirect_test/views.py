import random

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import User


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def simple_form(request):
    if request.method == 'POST':
        User.objects.create(name=f'John{random.randrange(100,999)}')
        return redirect(reverse('redirect_test:form'))
    users = User.objects.all()
    return render(request, 'index.html', context={'names': users})