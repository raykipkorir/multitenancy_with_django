from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ProjectForm
from .models import Project


class ProjectView(CreateView, ListView):
    form_class = ProjectForm
    template_name = "projects/projects.html"
    context_object_name = "projects"
    queryset = Project.objects.all()
    success_url = reverse_lazy("projects")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tenant"] = self.request.tenant.schema_name
        return context
    