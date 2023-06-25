from django.shortcuts import render

def appHome(request):
    return render(request, 'index.html')

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