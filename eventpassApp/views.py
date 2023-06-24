from django.shortcuts import render

def appHome(request):
    return render(request, 'index.html')