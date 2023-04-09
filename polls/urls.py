from django.urls import path
from . import views
from .views import SignUpView

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path ("vote/", views.vote, name="vote"),
    path ("vote/success", views.vote_success, name="success"),
    path ("vote/waiting", views.waiting_view, name="waiting"),
    path('results/', views.results, name='results'),
]