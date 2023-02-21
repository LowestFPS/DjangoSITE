from django.urls import path

from . import views


urlpatterns = [
    path("", views.AuthorizationView.as_view(), name="signin"),
]
