from django.contrib import admin

from .models import Profile, Skill, Project, SocialMedia, ContactMe


admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(SocialMedia)
admin.site.register(ContactMe)
