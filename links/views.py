from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import timezone
from .forms import LinkForm, LoginForm
from .models import Link


def index(request):
    form = LoginForm()
    return TemplateResponse(request, 'links/index.html', {'form': form})


# Create your views here.
def link_list(request):
    links = Link.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return TemplateResponse(request, 'links/link_list.html', {'links': links })

def userpage(request):
    return TemplateResponse(request, 'links/userpage.html', {})

def add(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            print("chek and get")
            new_link = Link(author=request.user, title=form.cleaned_data['title'], taglist = form.cleaned_data['tags'], text=form.cleaned_data['url'], created_date=timezone.now())
            new_link.save()
            return HttpResponse("Запись добавлена в базу данных <a href=''>Вернуться</a>")
    else:
        form = LinkForm()
        return TemplateResponse(request, 'links/add_link.html', {'form': form})

def logout(request):
    logout(request)

def login(request):

    login(request)

def remove(request):
    print("gone")
    return TemplateResponse(request, 'links/remove_link.html', {})

def newuser(request):
    return TemplateResponse(request, 'links/newuser.html', {})