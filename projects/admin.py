from django.contrib import admin

from django.apps import apps
from django_tenants.utils import get_public_schema_name


class ProjectsAdmin(admin.ModelAdmin):
    def has_view_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return False
        else:
            return True
    
    def has_add_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return False
        else:
            return True
    
    def has_change_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return False
        else:
            return True
    
    def has_delete_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return False
        else:
            return True
    
    def has_view_or_change_permission(self, request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return False
        else:
            return True
    
app = apps.get_app_config('projects')
for model_name, model in app.models.items():
    admin.site.register(model, ProjectsAdmin)
