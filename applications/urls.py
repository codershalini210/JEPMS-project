from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("employers/", views.employer_list, name="employer_list"),
    path("vacancies/", views.vacancy_list, name="vacancy_list"),
    path("applications/", views.application_list,
         name="application_list"),
]
