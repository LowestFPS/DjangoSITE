from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include


urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("main_app.urls")),
                  path("blog/", include("blog_app.urls")),
                  path("contacts/", include("feedback_app.urls")),
                  path("signup/", include("registration_app.urls")),
                  path("signin/", include("authorization_app.urls")),
                  path("search/", include("search_app.urls")),
                  path("ckeditor/", include("ckeditor_uploader.urls")),
                  path(
                      "signout/",
                      LogoutView.as_view(),
                      {"next_page": settings.LOGOUT_REDIRECT_URL},
                      name="signout",
                  ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
