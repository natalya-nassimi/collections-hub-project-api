from django.urls import path
from .views import CollectionListCreateView, CollectionDetailView, ItemCreateView, ItemDetailView, MyCollectionsView, MyProfileView

urlpatterns = [
    path('', CollectionListCreateView.as_view()),
    path('<int:pk>/', CollectionDetailView.as_view()),
    path('<int:collection_id>/items/', ItemCreateView.as_view()),
    path('<int:collection_id>/items/<int:pk>/', ItemDetailView.as_view()),
    path('mine/', MyCollectionsView.as_view()),
    path('profile/me/', MyProfileView.as_view())
]