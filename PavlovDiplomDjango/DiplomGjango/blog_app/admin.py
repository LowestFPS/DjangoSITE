from django.contrib import admin

from .models import PostModel


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostModel, PostAdmin)
