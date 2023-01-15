from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/books/", include("books.urls")),
    path(
        "openapi",
        get_schema_view(
            title="Django API - Book",
            description="POC of Django Deploy",
            version="1.0.0"
        ), name="openapi-schema"
    ),
    path(
        "swagger-ui/", 
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"}
        ), name="swagger-ui"
    ),
]
