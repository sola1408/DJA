from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Geography, Demand, Skills
from .hh import vacs

def main_page(request):
    template = loader.get_template('pages/main.html')
    context = {'title': "Главная"}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def geography(request):
    template = loader.get_template('pages/geography.html')
    topics = Geography.objects.all()
    context = {'title': "География", 'objects': topics}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def demand(request):
    template = loader.get_template('pages/demand.html')
    topics = Demand.objects.all()
    context = {'title': "Требования", 'objects': topics}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def skills(request):
    template = loader.get_template('pages/skills.html')
    topics2021 = Skills.objects.all().filter(year='2021').order_by('key_skills')
    topics2022 = Skills.objects.all().filter(year='2022').order_by('key_skills')
    topics = zip(topics2021, topics2022)
    context = {'title': "Скиллы", 'objects': topics}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def vacancies(request):
    template = loader.get_template('pages/vacancies.html')
    data = vacs()
    context = {'title': "Вакансии", 'objects': data}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)