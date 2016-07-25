from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import *

def index(request):
	return HttpResponse("Hello Tangeneers!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def detail(request, tangeneer_id):

	template = "hr/detail.html"

	context = {'tangeneer': 'Someones details'}

	return render(request, template, context)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


