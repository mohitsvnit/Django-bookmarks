from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render


def main_page(request):

    return render(request, 'home.html', {'user': request.user})


'''
def main_page(request):
    return render_to_response(
            'home.html',
            {'user': request.user}
    )

'''


def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')

    bookmarks = user.bookmark_set.all()

    template = get_template('user_name.html')
    var = Context({
        'username': 'username',
        'bookmarks': bookmarks,
    })

    output = template.render(var)
    return HttpResponse(output)
