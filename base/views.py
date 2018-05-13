from django.shortcuts import get_object_or_404, render

from .models import Competency


def index(request):
    """Home page."""
    return render(request, 'base/index.html', {})


def competency_list(request):
    """Home page."""
    competencies = Competency.objects.order_by('used_from_date')
    context = {'competencies': competencies}

    return render(request, 'base/competency_list.html', context)


def competency_detail(request, competency_id):
    """Competency Detail Page."""
    competency = get_object_or_404(Competency, pk=competency_id)
    return render(request, 'base/competency_detail.html',
                  {'competency': competency})
