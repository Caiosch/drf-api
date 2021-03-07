# from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('helloapp.urls')),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
