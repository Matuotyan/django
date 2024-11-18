from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Job

def base(request):
    return render(request,'jobs/base.html')
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def application_confirmation(request):
    return render(request, 'jobs/application_confirmation.html')
@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(id=job_id)
    Application.objects.create(job=job, user=request.user)
    return redirect('application_confirmation')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def job_list(request):
    if request.user.is_authenticated:
        jobs = Job.objects.all()
    else:
        jobs = Job.objects.filter(is_public=True)  # publicな求人のみ
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
# jobs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Job, Application
@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    # ユーザーが既にこの求人に応募しているか確認
    if Application.objects.filter(job=job, user=request.user).exists():
        # すでに応募済みの場合の処理
        return redirect('application_confirmation')
    
    # 新しい応募を作成
    Application.objects.create(job=job, user=request.user)
    
    return redirect('application_confirmation')
# jobs/views.py
