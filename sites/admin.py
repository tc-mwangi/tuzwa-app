from django.contrib import admin
from sites.models import Category, Country, Project, Profile, Rating, Follow


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar', 'title' ,'screenshot', 'description', 'link', 'country')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio', 'project', 'email')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('nominee', 'design', 'usability', 'creativity', 'content', 'overall_score', 'project')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')


admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Follow, FollowAdmin)


