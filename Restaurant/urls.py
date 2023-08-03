from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.sayHello, name="sayHello"),
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("static/", views.index, name="index"),
    path("menu/", views.MenuView.as_view()),
    path("booking/", views.BookingView.as_view()),
    path("api-token-auth/", obtain_auth_token),
]
