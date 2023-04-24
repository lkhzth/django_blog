from django.urls import path

from single_pages import views

urlpatterns = [
    path('', views.main),
    path('about_me', views.about_me),
]
