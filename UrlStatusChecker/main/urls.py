from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("check-url/<path:link>/", views.check_url, name="check-url"),
]