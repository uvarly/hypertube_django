from django.urls import path, include

urlpatterns = [
    path('local/', include('djoser.urls')),
    path('social/', include('rest_framework_social_oauth2.urls'))
]