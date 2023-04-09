from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path ("vote/", views.vote, name="vote"),
    path ("vote/success", views.vote_success, name="success"),
    path ("vote/waiting", views.waiting_view, name="waiting"),
    
]