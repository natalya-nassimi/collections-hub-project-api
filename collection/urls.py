from django.urls import path
from .views import CollectionListCreateView, CollectionDetailView

urlpatterns = [
    path('', CollectionListCreateView.as_view()),
    path('<int:pk>/', CollectionDetailView.as_view()),
]