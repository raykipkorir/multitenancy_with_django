from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django_tenants.admin import TenantAdminMixin
from django_tenants.utils import get_public_schema_name

from .models import Client, Domain


class TenantsAdmin(admin.ModelAdmin):
    '''
    Hides public models from tenants
    '''
    def has_view_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return True
        else:
            return False
    
    def has_add_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return True
        else:
            return False
    
    def has_change_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return True
        else:
            return False
    
    def has_delete_permission(self,request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return True
        else:
            return False
    
    def has_view_or_change_permission(self, request, view=None):
        if request.tenant.schema_name == get_public_schema_name():
            return True
        else:
            return False
    
# app = apps.get_app_config('tenants')
# for model_name, model in app.models.items():
#     admin.site.register(model, TenantsAdmin)

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, TenantsAdmin):
    list_display = ("name", "paid_until")


@admin.register(Domain)
class DomainAdmin(TenantsAdmin):
    list_display = ("domain", "tenant", "is_primary")


admin.site.unregister(User)
admin.site.register(User, TenantsAdmin)
admin.site.unregister(Group)
admin.site.register(Group, TenantsAdmin)
