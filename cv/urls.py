from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from cv import views


urlpatterns = [

        url(r'^$', views.Login, name='Main'),
        url(r'^login/$', views.Login, name='Login'),
        url(r'^newuser/$', views.NewUser, name='NewUser'),
        url(r'^(?P<userinfo>.+)/cvform$', views.BaseForm, name='BaseForm'),
        url(r'^(?P<userinfo>.+)/preview$', views.Preview, name='Preview'),
        url(r'^contact', views.contact, name='contact'),
        url(r'^send_mail$', views.send_mail, name='send_mail'),
        url(r'^error$', views.error, name='error'),
        url(r'^(?P<userinfo>.+)/pdf$', views.pdf, name='pdf'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)