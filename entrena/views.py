from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404

from .models import Node, Room, Room_Node, Reg_Node
from .forms import NodeForm, RoomForm, RoomNodeForm, RegNodeForm

def get_vebose_names(model):
    fields = []

    for field in model._meta.fields:
        fields.append(field.verbose_name)

    return fields

class Index(TemplateView):
    template_name = 'entrena/index.html'

class NodeList(CreateView):
    form_class = NodeForm
    # success_url = 'node/list.html'
    template_name = 'entrena/node/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['node_list'] = Node.objects.all()

        return context

class RoomList(CreateView):
    form_class = RoomForm
    template_name = 'entrena/room/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['room_list'] = Room.objects.all()

        return context

class RoomNodeList(CreateView):
    form_class = RoomNodeForm
    template_name = 'entrena/room_node/list.html'

    def get_initial(self, **kwargs):
        room = get_object_or_404(Room, pk=self.kwargs['pk'])
        return {
            'room': room,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fields = get_vebose_names(Room_Node)

        context['fields'] = fields
        context['room'  ] = get_object_or_404(Room, pk=self.kwargs['pk'])
        context['room_node_list'] = Room_Node.objects.filter(room=self.kwargs['pk'])

        return context

class RegNodeList(ListView):
    template_name = 'entrena/reg_node/list.html'

    def get_queryset(self, **kwargs):
        return Reg_Node.objects.filter(room_node=self.kwargs['pk_node'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fields = get_vebose_names(Reg_Node)
        context['fields'] = fields
        context['node'] = get_object_or_404(Room_Node, pk=self.kwargs['pk_node'])
        context['room'] = get_object_or_404(Room, pk=self.kwargs['pk_room'])
        
        return context