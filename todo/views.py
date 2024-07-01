from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from rest_framework import permissions, viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
   """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes =  [] # [permissions.IsAuthenticated] > man kann nur darauf zugereifen wenn man eingeloggt ist
    
    def create(self, request):
        todo = Todo.objects.create(title=self.request.POST.get('title', ''),
                                   description=self.request.POST.get('description', ''),
                                   user=self.request.user,
                                   )
        serialized_obj = serializers.serialize('json', [todo])
        return HttpResponse(serialized_obj, content_type='application/json')
    
    
    