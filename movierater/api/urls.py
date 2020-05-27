from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('movies',views.MovieViewSet)
router.register('ratings',views.RatingViewSet)
router.register('users', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
