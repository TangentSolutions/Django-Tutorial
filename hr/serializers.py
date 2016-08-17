from rest_framework import serializers
from django.contrib.auth.models import User, Group
from hr.models import *

 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
