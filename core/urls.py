from django.contrib import admin
from django.urls import path

from projects.views import ProjectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProjectView.as_view(), name="projects")
]
