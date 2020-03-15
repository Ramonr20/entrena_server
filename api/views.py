from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import generics

from entrena.models import Reg_Node
from .serializers import RegNodeSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class GetNodeView(generics.RetrieveAPIView):
    # authentication_classes = [TokenAuthentication]    
    # permission_classes = [IsAuthenticated]

    serializer_class = RegNodeSerializer
    queryset = Reg_Node.objects.all()
    
    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        
        objs = get_list_or_404(queryset, room_node=self.kwargs['room_node'])
        if "notfound" not in queryset:
            return objs[0]
        return objs

class SetNodeView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]    
    # permission_classes = [IsAuthenticated]

    queryset = Reg_Node.objects.all()
    serializer_class = RegNodeSerializer