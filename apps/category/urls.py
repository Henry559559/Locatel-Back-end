from django.urls import path, include, re_path
from .views import ListCategoriesView

urlpatterns = [
    path('categories', ListCategoriesView.as_view()),
]
