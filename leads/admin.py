from django.contrib import admin

from .models import User, Lead, Agent, UserProfile

# admin/admin    agent/admin
# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
