from rest_framework import viewsets
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=False, methods=['get'], url_path='list-cache')
    @method_decorator(cache_page(60))
    def list_cache(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)