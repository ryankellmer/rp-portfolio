from django.contrib import admin
from .models import AboutMe, Profile, Category, Skills, Project

admin.site.register(AboutMe)

class ProfileInline(admin.TabularInline):
        model = Profile
        extra = 1


class AboutMeAdmin(admin.ModelAdmin):
        inlines = [
                ProfileInline,
        ]

class SkillsInline(admin.TabularInline):
        model = Skills
        extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
        inlines = [
                SkillsInline,
        ]

admin.site.register(Project)
