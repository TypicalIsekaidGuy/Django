from django.urls import path

from .views import *


urlpatterns = [
    path('', index.as_view(), name='home'),
    path('upload/', upload, name='admin_upload'),
    path('logout/', logout_user, name='logout'),
    path('send/', send, name='admin_send'),
    path('request/', request, name='request'),
]