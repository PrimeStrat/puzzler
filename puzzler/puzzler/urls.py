from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("puzzle_app/", include("puzzle_app.urls")),
    path("admin/", admin.site.urls),
]