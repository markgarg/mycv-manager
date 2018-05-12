from django.shortcuts import render
from django.http import HttpResponse

from .models import Competency


def index(request):
    """Home page."""
    competencies = Competency.objects.order_by('used_from_date')
    output_text = "<h1>Hello, I'm Rohit Macherla</h1> <br /><br /><br />"
    output_text += "<br />".join([str(c) for c in competencies])
    return HttpResponse(output_text)
