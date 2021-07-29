from django.shortcuts import render
from projects.models import Project

def project_index(request):
        projects = Project.objects.all()        # query: allows to create, retrieve, update, or delete objects in your database.
        context = {     # Dictionary that is used to send information to my template.
                'projects': projects            
        }
        return render(request, 'project_index.html', context)  # Entries added to the context are available in the template.
        

def project_detail(request, pk):
        project = Project.objects.get(pk=pk)    # query retrieves the project with primary key.
        context = {     # Dictionary gets assigned the project
                'project': project
        }
        return render(request, 'project_detail.html', context)  # Project will pass to render(). 
