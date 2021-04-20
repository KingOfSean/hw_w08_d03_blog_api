from .models import Homework
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class HomeworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'title', 'body']