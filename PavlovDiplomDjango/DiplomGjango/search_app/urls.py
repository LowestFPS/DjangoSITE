from django.urls import path
from . import views


urlpatterns = [
    path("", views.SearchResultsView.as_view(), name="search_result"),
    path("tag/<slug:slug>/", views.TagView.as_view(), name="tag"),
]
