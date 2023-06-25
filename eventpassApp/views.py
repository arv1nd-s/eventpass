from django.shortcuts import render

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
        pass
    else:
        return render(request, 'event_create_form.html')