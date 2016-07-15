from django.contrib import admin

from .models import *

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'due_date')

class SkillAdmin(admin.ModelAdmin):
	pass

class JobAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'is_active')
	list_filter = ('category',)
	ordering = ('-created',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Job, JobAdmin)