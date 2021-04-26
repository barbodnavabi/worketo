from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class UserInfoCreateView(CreateView):
    model = UserInfo
    template_name = "resume/user_info_create.html"


class StudyCreateView(CreateView):
    model = Study
    template_name = "study_create.html"



class SkillCreateView(CreateView):
    model = Skill
    template_name = "skill_create.html"



class ProjectCreateView(CreateView):
    model = Project
    template_name = "project_create.html"


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = "experience_create.html"
