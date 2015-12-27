from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext
from bookmarks.forms import *


def main_page(request):
    c = {'user': request.user}

    return render(request, 'home.html', c, RequestContext(request))


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')

    bookmarks = user.bookmark_set.all()
    var = {
        'username': 'username',
        'bookmarks': bookmarks,
    }

    return render(request, 'user_name.html', var, RequestContext(request))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password= form.cleaned_data['password1'],
                email= form.cleaned_data['email']
            )

            return HttpResponseRedirect('/register_successful/')
    else:
        form = RegistrationForm()
    var = {
        'form': form
    }
    return render(request, 'registration/register.html', var, RequestContext(request))
