from django.urls import path, include

from . import views
from .views import SignUpView


app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("view-categories/", views.viewcategories, name="viewcategories"),

    path("nomination_category/<int:nomination_category_id>/", views.nomination_category_detail, name="nomination_category_detail"),
    path("category/<int:category_id>/vote/", views.nominee_vote, name="nominee_vote"),
    path('category/<int:category_id>/results/', views.nomination_category_results, name='nomination_category_results'),
    path('not_registered/', views.not_registered, name='not_registered'),
    path('thankyou/', views.thank_you_forvoting, name='thank_you_forvoting'),
    path('vote_limit/', views.vote_limit, name='vote_limit'),

    
    # ACCOUNT URLS
    path("signup/", SignUpView.as_view(), name="signup"),

]
