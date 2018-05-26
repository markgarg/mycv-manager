from django.shortcuts import get_object_or_404, render
import json

from .models import Competency, Company


def index(request):
    """Home page."""
    return render(request, 'base/index.html', {})


def competency_list(request):
    """Home page."""
    competencies = (Competency.objects
                    .order_by('used_from_date')
                    .values('name', 'weight'))
    print('competencies :', json.dumps(list(competencies)))
    context = {'competencies': json.dumps(list(competencies))}

    return render(request, 'base/competency_list.html', context)


def competency_detail(request, competency_name):
    """Competency detail page."""
    competency = get_object_or_404(Competency, pk=competency_name.lower())
    return render(request, 'base/competency_detail.html',
                  {'competency': competency})


def company_list(request):
    """Home page."""
    companies = (Company.objects.values('name', 'url'))
    print('companies :', json.dumps(list(companies)))
    context = {'companies': json.dumps(list(companies))}

    return render(request, 'base/company_list.html', context)


def company_detail(request, company_id):
    """Company detail page."""
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'base/company_detail.html',
                  {'company': company})


def about_site(request):
    """About the website."""
    return render(request, 'base/about_site.html', {})
