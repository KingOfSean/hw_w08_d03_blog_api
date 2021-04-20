from .models import Homework
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HomeworkSerializer
class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [permissions.AllowAny]