from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from authenticate.models import Profile

from .models import remainders

@login_required
def main(request):
    if request.method=="POST":
        temp1 = request.user
        title = request.POST.get('title')
        task = request.POST.get('task')
        date = request.POST.get('date')
        time = request.POST.get('timer')
        try:
            ask = Profile.objects.get(user = temp1)
        except:
                print("Incomplete Profile")
                return redirect('/complete-profile')
        print(ask.count)
        if(ask.count>5):
            if(not ask.purchased):
                return render(request,'plans.html')
        
        ask.count+=1
        ask.save()
        post = remainders()
        post.user = temp1
        post.title = title
        post.task = task
        post.date = date
        post.timer = time
        post.save()
        messages.success(request,'successfully added '+title)
        return render(request,'index.html')
    return render(request,'index.html')

@login_required
def myrem(request):
    a = remainders.objects.filter(user = request.user)
    latest_question_list = a
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'myrem.html',context)

def default(request):
    if request.user.is_authenticated:
        return redirect('Homepage')
    else:
        return render(request,'homepage.html')

def accounts(request):
    return render(request,'accounts.html')

def delete(request):
    if request.method=="POST":
        post = remainders()
        val = request.POST.get('title')
        print(val)
        instance = remainders.objects.get(title =val)
        print(instance)
        instance.delete()
        return redirect('myreminders')
    return render(request,'deletion.html')

@login_required
def complete_profile(request):
    a = request.user
    try:
        print(a)
        Profile.objects.get(user = a)
        print('-----------------')
        return redirect('/reminders/')
    except:
        return render(request,'profile.html')
    if request.method=='POST':
        usr = request.user
        fnmae = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pfle = Profile()
        pfle.user = usr
        pfle.first_name = fnmae
        pfle.last_name = lname
        pfle.email = email
        pfle.save()
        return redirect('')