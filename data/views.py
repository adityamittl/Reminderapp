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
        ask = Profile.objects.get(user = temp1)
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
