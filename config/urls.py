from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.admin import AdminSite


urlpatterns = [
    path("", include("polls.urls")),
    path('dashboard/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
AdminSite.site_header = 'Mombasa Youths Awards'
AdminSite.site_title = 'Mombasa Youths Awards'
AdminSite.index_title = 'Mombasa Youths Awards'
