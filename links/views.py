from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from .forms import LinkForm, LoginForm, SignUpForm, SearchForm
from .models import Link
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def index(request):
    form = LoginForm()
    return TemplateResponse(request, 'links/index.html', {'form': form})


# Create your views here.
def list(request):
    links = Link.objects.filter(created_date__lte=timezone.now()).filter(author=request.user).order_by('-created_date')
    return TemplateResponse(request, 'links/list.html', {'links': links})

def tagview(request, tag):
    links = Link.objects.filter(author=request.user).filter(taglist__icontains=tag).order_by('-created_date')
    return TemplateResponse(request, 'links/list.html', {'links': links})


def userpage(request):
    form = SearchForm()
    total = Link.objects.filter(author=request.user).count()

    tags = Link.objects.filter(author=request.user).values_list('taglist')
    links_l = []
    links = []
    for tag in tags:
        a = ' '.join(tag)
        links_l.append(a.lower())

    for x in links_l:
        b = x.split(" ")
        for i in b:
            i = i.lower()
            links.append(i)

    dict_tag = {}
    for link in links:
        link = link.lower()
        if link in dict_tag.keys():
            dict_tag[link] += 1
        else:
            dict_tag[link] = 1

    return TemplateResponse(request, 'links/userpage.html', {'links':dict_tag, 'total':total, 'form':form})


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
        return TemplateResponse(request, 'links/add.html', {'form': form})


def logout(request):
    logout(request)

def remove(request):
    print("gone")
    return TemplateResponse(request, 'links/remove.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('userpage')
    else:
        form = SignUpForm()
    return render(request, 'links/signup.html', {'form': form})