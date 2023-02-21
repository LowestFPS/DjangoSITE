from django.urls import path

from . import views


urlpatterns = [
    path("", views.FeedBackView.as_view(), name="contacts"),
    path("thanks/", views.ThanksView.as_view(), name="thanks"),
]
