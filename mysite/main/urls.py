from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('geography', views.geography, name='geography'),
    path('demand', views.demand, name='demand'),
    path('skills', views.skills, name='skills'),
    path('vacancies', views.vacancies, name='vacancies'),
]