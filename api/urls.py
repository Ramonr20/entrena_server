from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include 
from api import views

urlpatterns = [
        path('sensores/', views.SetNodeView.as_view()),
        path('sensores/<int:room_node>', views.GetNodeView.as_view()),
        path('sensores/<int:room_node>/all', views.GetNodeAllView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
