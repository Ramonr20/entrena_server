from entrena.models import Node, Room, Room_Node, Reg_Node
from rest_framework import serializers

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Node
        fields = '__all__'

class RegNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Node
        fields = '__all__'