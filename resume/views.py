from django.shortcuts import render,reverse
from django.views.generic import CreateView


class UserInfoCreateView(CreateView):
    model = UserInfo
    template_name = "resume/user_info_create.html"
    success_url = reverse('study-create')


class StudyCreateView(CreateView):
    model = Study
    template_name = "study_create.html"
    success_url = reverse('experience-create')




class SkillCreateView(CreateView):
    model = Skill
    template_name = "skill_create.html"
    success_url = reverse('project-create')



class ProjectCreateView(CreateView):
    model = Project
    template_name = "project_create.html"
    success_url = reverse('skill-create')


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = "experience_create.html"
    success_url=reverse('index')

