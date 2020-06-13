from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from entrena.models import Reg_Node
from .serializers import RegNodeSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from datetime import date, timedelta
from django.utils import timezone

class GetNodeView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = RegNodeSerializer
    queryset = Reg_Node.objects.all()
    
    def get_object(self, **kwargs):
        queryset = self.get_queryset()
        
        objs = get_list_or_404(queryset, room_node=self.kwargs['room_node'])
        if "notfound" not in queryset:
            return objs[0]
        return objs

class GetNodeAllView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None, **kwargs):

        end_date = timezone.now()
        start_date = end_date - timedelta(days=14)
        reg_sensors = Reg_Node.objects.filter(room_node=self.kwargs['room_node'], date__range=[start_date, end_date]).order_by('date')
        
        data = {
            'voltaje': [reg.voltaje for reg in reg_sensors],
            'corriente':[reg.corriente for reg in reg_sensors],
            'fac_de_pot':[reg.fac_de_pot for reg in reg_sensors],
            'pot_activa':[reg.pot_activa for reg in reg_sensors],
            'pot_real':[reg.pot_real for reg in reg_sensors],
            'pot_aparente':[reg.pot_aparente for reg in reg_sensors],
            'date':[reg.date for reg in reg_sensors]
        }
        return Response(data)

class SetNodeView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Reg_Node.objects.all()
    serializer_class = RegNodeSerializer