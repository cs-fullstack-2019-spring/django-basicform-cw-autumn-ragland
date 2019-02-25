from django.urls import path
from . import views

# paths accessed through html actions
urlpatterns = [
    path("", views.index, name="index"),
    path("displayName/", views.displayName, name="displayName"),
    path("addFive/<int:accountID>", views.addFive, name="addFive"),
]
