from .views import *
urlpatterns = [
    path("user-info/create", UserInfoCreateView.as_view(), name="userinfo-create")
    path("study/create", StudyCreateView.as_view(), name="study-create")
    path("skill/create", SkillCreateView.as_view(), name="skill-create")
    path("project/create", ProjectCreateView.as_view(), name="project-create")
    path("experience/create", ExperienceCreateView.as_view(), name="experience-create")
]
