from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event, Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

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
        return redirect('/login')

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


def eventsPage(request):
    # fill events into the template

    return render(request, 'events.html', context={'user': request.user})


def createEvent(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form_data = request.POST.dict()

            event_data = Event(
                title=form_data.get("event-title"),
                city=form_data.get("location-city"),
                user_id=User.objects.get(id=request.user.id),
                starts_at=form_data.get("start-date-time"),
                ends_at=form_data.get("end-date-time"),
                address=form_data.get("location-address"),
                pincode=form_data.get("location-pincode"),
                category=form_data.get("event-type"),
                description=form_data.get("event-description"),
                image=request.FILES.get("image-upload"),
                ticket_price=form_data.get("ticket-price")
            )
            event_data.save()

            return redirect('/create-event')

        else:
            return render(request, 'event_create_form.html', context={'user': request.user})
        
    else:
        return redirect('/login')
    

def myTicketsList(request):
    if request.user.is_authenticated:
        # get the userid
        user_id = request.user.id
        # for that userid get the tickets record
        ticket_records = Booking.objects.filter(user_id=user_id)
        tickets_data = []
        for t_record in ticket_records:
            ticket = {}
            event_record = t_record.event_id
            ticket['id'] = t_record.id
            ticket['event_name'] = event_record.title
            ticket['dateTime'] = event_record.starts_at
            ticket['location'] = event_record.city
            tickets_data.append(ticket)
        
        # pass to the template
        return render(request, 'mytickets.html', context={'tickets_data': tickets_data})
    else:
        return redirect('/login')


def showTicket(request):
    ticket_id = request.GET.get('id')
    user_id = request.user.id
    ticket_record = Booking.objects.get(id=ticket_id)
    # check if this userid have access to the request ticket using ticket id
    if ticket_record.user_id.id == user_id:
        ticket = {}
        ticket['id'] = ticket_record.id
        ticket['ename'] = ticket_record.event_id.title
        ticket['dateTime'] = ticket_record.event_id.starts_at
        ticket['location'] = ticket_record.event_id.city
        ticket['holder'] = ticket_record.user_id.first_name

        return render(request, 'ticket.html', context={'ticket': ticket})
    else:
        return redirect('/my-tickets')
        

def searchResults(request):
    if request.GET.get('search-type') == 'name':
        user_search = request.GET.get('query')
        event_records = Event.objects.filter(title__icontains=user_search)
        return render(request, 'events.html', context={'event_records': event_records})

    elif request.GET.get('search-type') == 'location':
        user_search = request.GET.get('query')
        event_records = Event.objects.filter(city__icontains=user_search)

        for event in event_records:
            print(event.__dict__)

        return render(request, 'events.html', context={'event_records': event_records})
    
    elif request.GET.get('query'):
        # By city and title
        user_search = request.GET.get('query')

        query = Q(title__icontains=user_search)
        query.add(Q(city__icontains=user_search), Q.OR)

        event_records = Event.objects.filter(query)

        return render(request, 'events.html', context={'event_records': event_records})

    else:
        return redirect('/')

def viewEvent(request):
    event_id = request.GET.get('id')
    if event_id:
        event = Event.objects.get(id=event_id)
        organizer = User.objects.get(id=event.user_id_id).first_name
        return render(request, 'view_event.html', context={'event': event, 'organizer': organizer})
    else:
        return HttpResponse(status=204)

def buyTicket(request):
    if request.user.is_authenticated:
        event_id = request.GET.get('id')

        event_record = Event.objects.get(id=event_id)
        user_record = User.objects.get(id=request.user.id)
        Booking.objects.create(
            event_id=event_record,
            user_id=user_record
        )
        return redirect('/my-tickets')

    else:
        return redirect('/login')