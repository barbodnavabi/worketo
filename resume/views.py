from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import UserInfo,Study,Skill,Project,Experience
from .mixins import FormUserMixin
class UserInfoCreateView(FormUserMixin,CreateView):
    model = UserInfo
    fields=["full_name","email","phone","image","address","bio","github","linkendin","website","facebook","instagram",
    "telegram","whatsApp",]
    template_name = "resume/user_info_create.html"


class StudyCreateView(FormUserMixin,CreateView):
    model = Study
    fields=["course","college",'description']
    template_name = "resume/study_create.html"
    success_url=reverse_lazy("study-create")
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["studies"] = Study.objects.filter(user=self.request.user)
            return context
        




class SkillCreateView(CreateView):
    model = Skill
    template_name = "skill_create.html"



class ProjectCreateView(CreateView):
    model = Project
    template_name = "project_create.html"


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = "experience_create.html"

