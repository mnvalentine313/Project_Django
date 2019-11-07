from django.shortcuts import render, redirect

from .models import User, Video
from .forms import UserForm, VideoForm
from django.contrib.auth.decorators import login_required

def users_list(request):
    users = User.objects.all()
    videos = Video.objects.all()
    return render(request, 'youtubify/users_list.html', {'users': users, 'videos': videos})

@login_required
def user_detail(request, pk):
    user = User.objects.get(id=pk)
    return render(request, 'youtubify/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'youtubify/user_form.html', {'form': form})

@login_required
def user_edit(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'youtubify/user_form.html', {'form': form})

@login_required
def user_delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('users_list')

def videos_list(request):
    videos = Video.objects.all()
    return render(request, 'youtubify/videos_list.html', {'videos': videos})

@login_required
def video_detail(request, pk):
    video = Video.objects.get(id=pk)
    return render(request, 'youtubify/video_detail.html', {'video': video})

@login_required
def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm()
    return render(request, 'youtubify/video_form.html', {'form': form})

@login_required
def video_edit(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save()
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'youtubify/video_form.html', {'form': form}) 

def video_delete(request, pk):
    Video.objects.get(id=pk).delete()
    return redirect('users_list')