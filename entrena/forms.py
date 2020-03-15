from django.forms import ModelForm, HiddenInput
from .models import Node, Room, Room_Node, Reg_Node

class NodeForm(ModelForm):
    class Meta():
        model = Node
        fields = ['tipo_nodo']

class RoomForm(ModelForm):
    class Meta():
        model = Room
        fields = ['nombre_hab']

class RoomNodeForm(ModelForm):
    class Meta():
        model = Room_Node
        fields = '__all__'
        widgets = {
            'room': HiddenInput(),
        }

class RegNodeForm(ModelForm):
    class Meta():
        model = Reg_Node
        fields = '__all__'