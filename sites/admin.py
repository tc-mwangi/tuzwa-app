from django.contrib import admin
from sites.models import Project, Profile 


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'screenshot', 'description', 'link')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar', 'bio', 'title','screenshot', 'description', 'link', 'email')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)



