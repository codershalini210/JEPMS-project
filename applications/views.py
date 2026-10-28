from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Employer, Vacancy, JobApplication
 
 
@login_required
def dashboard(request):
    return render(request, "dashboard.html", {
        "employer_count": Employer.objects.count(),
        "vacancy_count": Vacancy.objects.count(),
        "application_count": JobApplication.objects.count(),
    })
 
 
@login_required
def employer_list(request):
    return render(request, "employers/list.html", {
        "employers": Employer.objects.all(),
    })
 
 
@login_required
def vacancy_list(request):
    return render(request, "vacancies/list.html", {
        "vacancies": Vacancy.objects.select_related("employer"),
    })
 
 
@login_required
def application_list(request):
    return render(request, "applications/list.html", {
        "applications": JobApplication.objects.select_related(
            "vacancy", "vacancy__employer"
        ),
    })
