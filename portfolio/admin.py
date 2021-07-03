from django.contrib import admin
from .models import Project

class MyModelAdmin(admin.ModelAdmin):

    # Delete Multiple Items from django-admin
    # Which Uses Query-set
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

admin.site.register(Project,MyModelAdmin)