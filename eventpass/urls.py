"""
URL configuration for eventpass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventpassApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', appHome, name='Home'),

    path('login/', loginUser, name='Login'),

    path('signup/', signup, name='Signup'),
 
    path('logout/', logoutUser, name='Logout'),

    path('profile/', profile, name='Profile'),

    path('search/', searchResults, name='SearchResults'),

    path('events/', eventsPage, name='EventsPage'),

    path('view-event/', viewEvent, name='ViewEvent'),

    path('create-event/', createEvent, name='CreateEvent'),

    path('buy-ticket/', buyTicket, name='BuyTicket'),

    path('my-tickets/', myTicketsList, name='MyTickets'),

    path('ticket/', showTicket, name='Ticket'),
 
    path('about/', about, name='About'),

    path('admin/', admin.site.urls),
]

# https://testdriven.io/blog/django-static-files/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)