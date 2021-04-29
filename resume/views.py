from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Study,Skill,Project,Experience
from .mixins import FormUserMixin


class StudyCreateView(FormUserMixin,CreateView):
    model = Study
    fields=["course","college",'description']
    template_name = "resume/study_create.html"
    success_url=reverse_lazy("study-create")
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["studies"] = Study.objects.filter(user=self.request.user)
            return context
        




class SkillCreateView(FormUserMixin,CreateView):
    model = Skill
    success_url=reverse_lazy("skill-create")
    fields =["skill","percent",]
    template_name = "resume/skill_create.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["Skills"] = Skill.objects.filter(user=self.request.user)
            return context



class ProjectCreateView(FormUserMixin,CreateView):
    model = Project
    template_name = "resume/project_create.html"
    success_url=reverse_lazy("project-create")
    fields=["name","type",'image','link','description']
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["projects"] = Project.objects.filter(user=self.request.user)
            return context


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = "experience_create.html"

