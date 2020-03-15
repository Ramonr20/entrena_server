from django.urls import path
from entrena import views

app_name = 'entrena'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('nodos/', views.NodeList.as_view(), name='lista_nodes'),
    path('habitaciones/', views.RoomList.as_view(), name='lista_rooms'),

    path('habitaciones/<int:pk>/nodos/', views.RoomNodeList.as_view(), name='lista_room_node'),
    path('habitaciones/<int:pk_room>/nodos/<str:pk_node>', views.RegNodeList.as_view(), name='lista_reg_node')
]

