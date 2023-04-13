from django.urls import path, include

from . import views
from .views import SignUpView


app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("vote/", views.voteDetails, name="votedetails"),
    path("nomination_category/<int:nomination_category_id>/", views.nomination_category_detail, name="nomination_category_detail"),
    path("category/<int:category_id>/vote/", views.nominee_vote, name="nominee_vote"),
    path('category/<int:category_id>/results/', views.nomination_category_results, name='nomination_category_results'),
    
    # ACCOUNT URLS
    path("signup/", SignUpView.as_view(), name="signup"),

]
