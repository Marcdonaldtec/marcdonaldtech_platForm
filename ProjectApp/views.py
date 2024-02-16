from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm 
from django.contrib.auth.decorators import login_required
from UserApp import *


@login_required(login_url='AuthenticationApp:login')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            user_profile = request.user.userprofile
            project.user_profile = user_profile
            project.save()
            form.save_m2m() 
            return redirect('UserApp:user_profile', username=request.user.username)
    else:
        form = ProjectForm()

    return render(request, 'ProjectApp/create_project.html', {'form': form})

@login_required(login_url='AuthenticationApp:login')
def edit_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    if request.user == project.user_profile.user:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                return redirect('UserApp:user_profile', username=request.user.username)
        else:
            form = ProjectForm(instance=project)

        return render(request, 'ProjectApp/edit_project.html', {'form': form, 'project': project})
    return redirect('UserApp:user_profile', username=request.user.username)

@login_required(login_url='AuthenticationApp:login')
def delete_project(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    if request.user == project.user_profile.user:
        if request.method == 'POST':
            project.delete()
            return redirect('UserApp:user_profile', username=request.user.username)

        return render(request, 'ProjectApp/delete_project_confirm.html', {'project': project})

    return redirect('UserApp:user_profile', username=request.user.username)

@login_required(login_url='AuthenticationApp:login')
def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'ProjectApp/project_detail.html', {'project': project})
