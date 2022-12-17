from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
from .forms import *


class index(LoginView):
    form_class = AuthenticationForm
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('request')


def upload(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_upload')
    else:
        form = FilesForm()

    context = {
        'title': 'Загрузка файлов',
        'form': form
    }
    return render(request, 'core/stranicha2.html', context=context)


def send(request):
    if request.method == 'POST':
        form = MessagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_upload')
    else:
        form = MessagesForm()

    context = {
        'title': 'Отправка файлов',
        'form': form
    }

    return render(request, 'core/stranicha3.html', context=context)


def request(request):
    context = {
        'title': 'Отчеты',
    }
    return render(request, 'core/stranicha4.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound(f"Запрашиваемая страница не найдена")


def logout_user(request):
    logout(request)
    return redirect('home')
