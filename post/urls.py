from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostCollectionView.as_view()),
    path("<int:pk>/", views.PostSingletonView.as_view())
]
