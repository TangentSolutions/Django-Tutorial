from django.http import HttpResponse
import datetime
from django.shortcuts import render

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