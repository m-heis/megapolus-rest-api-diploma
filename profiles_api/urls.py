from django.urls import path

from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('saken-view/', views.SakenApiView.as_view()),
    path('family/', views.FamilyApiView.as_view())
]