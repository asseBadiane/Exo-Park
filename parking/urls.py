from django.urls import path
from .views import PlaceListAPIView, PlaceDetailAPIView

urlpatterns = [
    path('places/', PlaceListAPIView.as_view(), name='place-list'),
    path('places/<int:pk>/', PlaceDetailAPIView.as_view(), name='place-detail'),
]
