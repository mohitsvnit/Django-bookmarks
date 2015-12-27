"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.views.generic import TemplateView
import os.path

site_media = os.path.join(
        os.path.dirname(__file__), 'site_media'
)

urlpatterns = [
    url(r'^$', 'bookmarks.views.main_page'),
    url(r'^user/(\w+)/$', 'bookmarks.views.user_page'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'bookmarks.views.logout_page'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': site_media}),
    url(r'^register/$', 'bookmarks.views.register_page'),
    url(r'^register_successfull/$',TemplateView.as_view(template_name='registration/register_done.html')),
]
