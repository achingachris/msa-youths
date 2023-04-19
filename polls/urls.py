from django.urls import path
from . import views
from .views import SignUpView, NominationCategoryList, NomineesByCategory, NominationCategoryDetail

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("view-categories/", views.viewcategories, name="viewcategories"),
    path("nomination_category/<int:nomination_category_id>/", views.nomination_category_detail, name="nomination_category_detail"),
    path("category/<int:category_id>/vote/", views.nominee_vote, name="nominee_vote"),
    path('category/<int:category_id>/results/', views.nomination_category_results, name='nomination_category_results'),
    path('not_registered/', views.not_registered, name='not_registered'),
    path('thankyou/', views.thank_you_forvoting, name='thank_you_forvoting'),
    path('vote_limit/', views.vote_limit, name='vote_limit'),
    path("signup/", SignUpView.as_view(), name="signup"),
    
    # APIS
    path('api/categories/', NominationCategoryList.as_view(), name='categories'),
    path('api/categories/<int:category_id>/nominees/', NomineesByCategory.as_view(), name='nominees_by_category'),
    path('api/categories/<int:pk>/', NominationCategoryDetail.as_view(), name='nomination_category_detail'),



]
