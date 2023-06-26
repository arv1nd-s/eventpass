from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def appHome(request):
    return render(request, 'index.html', context={'user': request.user})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        
        user = User.objects.create(
            first_name = request.POST.get('name'),
            username = request.POST.get('email')
        )
        user.set_password(request.POST.get('password'))
        user.save()
        return HttpResponseRedirect('/login')

    else:
        return render(request, 'signup.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Usernaame')
            return redirect('/login/')
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)

        return redirect('/profile/')
    
    else:
        return render(request, "login.html")

def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    
    if request.user.is_authenticated:
        return render(request, 'logout.html', context={'user': request.user})
    else:
        return redirect('/login')


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", context={'user': request.user})
    else:
        return redirect('/login/')


def about(request):
    return render(request, 'about.html', context={'user': request.user})        

def searchResults(request):
    # get the searched event name or location

    # filter it out from db

    # fill into the template

    return render(request, 'search_results.html', context={'user': request.user})

def eventsPage(request):
    # fill events into the template

    return render(request, 'events.html', context={'user': request.user})

def createEvent(request):
    if request.method == "POST":
        form_data = request.POST.dict()
        print(form_data.items())

        event_data = Event(
            title=form_data.get("event-title"),
            city=form_data.get("location-city"),
            organizer=form_data.get("organizer"),
            user_id=1,
            # starts_at="",
            # ends_at="",
            address=form_data.get("location-address"),
            pincode=form_data.get("location-pincode"),
            category=form_data.get("event-type"),
            description=form_data.get("event-description"),
            image_path=""
        )
        event_data.save()

        return HttpResponseRedirect('/create-event')

    else:
        return render(request, 'event_create_form.html', context={'user': request.user})