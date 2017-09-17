from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import SignUpForm
from .models import Goal, Subtask
import datetime
import json
from pyrebase_settings import auth, db, user2

# Create your views here.
def firebase(request):

    digbick = db.child('users').get().val().values()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')

            auth.create_user_with_email_and_password(email, raw_password)
            db.child('users').push({
                username: {
                    'email': email,
                    'password': raw_password
                }
            })
            print('success')
            return redirect('index')
    else:
        form = SignUpForm()

        for dick in digbick:
            for bick in dick:
                print(bick)

    return render(request, 'track/firebase.html',{'form': form, 'digbick':digbick})
def index(request):
    golz = Goal.objects.all()
    subs = Subtask.objects.all()

    if request.method == 'POST':
        golz = Goal.objects.all();
        abc = request.POST.getlist('tite')
        goal_name = request.POST['gNamePost']
        desc = request.POST['gDescPost']
        due = request.POST['gDatePost']
        due = datetime.datetime.strptime(due, "%d/%m/%Y").strftime("%Y-%m-%d")

        goal = Goal(goal_name=goal_name,desc=desc,dueDateG=due)
        goal.save()
        for a in abc:
            subtsk = Subtask(goal_name=goal, task_name=a)
            subtsk.save()
        subs = Subtask.objects.all()
        return redirect('index')


    return render(request, 'track/index.html',{'goals': golz, 'subs': subs})

def completeTask(request):
    awch = "meh"
    if request.method == 'POST':
        curdate = datetime.datetime.today()
        subtask = Subtask.objects.get(task_name=request.POST['task_name'])
        subtask.doneDateS = curdate
        subtask.save()
        goal = Goal.objects.get(goal_name=subtask.goal_name.goal_name)

        stat = goal.get_Status()
        if stat == 100:
            goal.doneDateG = curdate
            awch = "completed"
    return JsonResponse({'aw': awch})


