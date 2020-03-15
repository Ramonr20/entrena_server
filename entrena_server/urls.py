from django.contrib import admin
from django.urls import path, include

# from api import views

# from rest_framework import routers

# router = routers.DefaultRouter()

# En el router vamos añadiendo los endpoints a los apiets
# router.register('registro/nodos', views.RegNodeViewSet)

urlpatterns = [

  #API url's
  # path('api/v1/', include(router.urls)),

  path('admin/', admin.site.urls),

  #entrena url's
  path('', include(('entrena.urls', 'vistas'), namespace='vistas')),
  
  path('api/v1/', include('api.urls')),

  # auth url's
  path('api/v1/auth/', include('rest_auth.urls')),
  path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
]
