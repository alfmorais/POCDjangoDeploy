from rest_framework.mixins import (
    CreateModelMixin, 
    DestroyModelMixin,
    ListModelMixin, 
    RetrieveModelMixin,
    UpdateModelMixin
)
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import GenericViewSet

from .models import Book
from .serializers import BookListSerializer


class BooksAPIViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    serializer_map = {
        "GET": BookListSerializer,
        "POST": BookListSerializer,
        "PUT": BookListSerializer,
        "DELETE": BookListSerializer,
    }
    queryset = Book.objects.all()
    lookup_url_kwarg = "id"
    lookup_field = "id"
    schema = AutoSchema(
        tags=["Books"],
        component_name="Book",
        operation_id_base="Book",
    )

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method)


book_list = BooksAPIViewSet.as_view({"get": "list", "post": "create"})
book_retrieve = BooksAPIViewSet.as_view({"get": "retrieve"})
