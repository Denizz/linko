from django.template.response import TemplateResponse
from django.utils import timezone

from .models import Link


def index(request):
    return TemplateResponse(request, 'links/index.html', {})


# Create your views here.
def link_list(request):
    links = Link.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return TemplateResponse(request, 'links/link_list.html', {'links': links })

def userpage(request):
    return TemplateResponse(request, 'links/userpage.html', {})

def add(request):
    return TemplateResponse(request, 'links/add_link.html', {})