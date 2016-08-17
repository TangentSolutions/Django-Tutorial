from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from hr import views

router = routers.DefaultRouter()

router.register(r'jobs', views.JobViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]