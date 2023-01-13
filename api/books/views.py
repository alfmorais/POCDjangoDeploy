from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet

from .models import Book
from .serializers import BookListSerializer


class BooksAPIViewSet(
    CreateModelMixin,
    # DestroyModelMixin,
    RetrieveModelMixin,
    # UpdateModelMixin,
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

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method)


book_list = BooksAPIViewSet.as_view({"get": "list", "post": "create"})
book_retrieve = BooksAPIViewSet.as_view({"get": "retrieve"})
