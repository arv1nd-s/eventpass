from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Event

def appHome(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'signup.html')

def loginPage(request):
    return render(request, "login.html")

def about(request):
    return render(request, 'about.html')

def searchResults(request):
    # get the searched event name or location

    # filter it out from db

    # fill into the template

    return render(request, 'search_results.html')

def eventsPage(request):
    # fill events into the template

    return render(request, 'events.html')

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
        # print(form_data.get("start-date"))
        # print(form_data.get("start-time"))
        # print(form_data.get("end-date"))
        # print(form_data.get("end-time"))
        # print(form_data.get("image-upload"))

        return HttpResponseRedirect('/create-event')

    else:
        return render(request, 'event_create_form.html')