from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # csrf_exempt to be able to test the view with postman
    url(r'^$', csrf_exempt(views.ExampleView.as_view())),
]
