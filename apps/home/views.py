from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


@login_required(login_url='/login/')
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/index.html', {'segment': 'index'})


@login_required(login_url='/login/')
def pages(request: HttpRequest) -> HttpResponse:
    load_template = request.path.split('/')[-1]

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))

    try:
        return render(request, f'home/{load_template}', {'segment': load_template})
    except template.TemplateDoesNotExist:
        return render(request, 'home/page-404.html', {})
    except Exception:
        return render(request, 'home/page-500.html', {})
