from django.urls import path

from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<slug:slug>/", views.detail, name="detail"),
    path("apropos/", views.apropos, name="apropos"),
    path("contact/", views.contact, name="contact")
]
