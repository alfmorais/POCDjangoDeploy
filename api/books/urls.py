from books import views
from django.urls import include, path

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:id>/", views.book_retrieve, name="book_retrieve"),
    # path("<id:int>/"),
    # path("<id:int>/"),
]
