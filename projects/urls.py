from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),   # root URL is hooked up to the project_index view.
        #path("<int:pk>/", views.project_detail, name="project_detail"), # Value passed in the URL is an integer named pk.
]