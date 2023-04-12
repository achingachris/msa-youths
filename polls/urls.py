from django.urls import path, include

from . import views
from .views import SignUpView


app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("nomination_category/<int:nomination_category_id>/", views.nomination_category_detail, name="nomination_category_detail"),
    path("category/<int:category_id>/vote/", views.nominee_vote, name="nominee_vote"),
    path('category/<int:category_id>/results/', views.nomination_category_results, name='nomination_category_results'),
    
    # ACCOUNT URLS
    path("signup/", SignUpView.as_view(), name="signup"),
    
]
