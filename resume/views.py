from django.shortcuts import render,reverse
from django.views.generic import CreateView
from .models import UserInfo,Study,Skill,Project,Experience

class UserInfoCreateView(CreateView):
    model = UserInfo
    fields=["user","full_name","email","phone","image","address","bio","github","linkendin","website","facebook","instagram",
    "telegram","whatsApp",]
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

