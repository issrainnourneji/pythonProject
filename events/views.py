from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,CreateView
from .forms import EventForm, EventModelForm
from django.urls import reverse_lazy

# Create your views here.

from .models import Event
# def homePage(request):
# def listEventStatic(request):

def addEvent(request):
    form = EventForm()
    if request.method =="POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
         Event.objects.create(title = form.cleaned_data)
        return redirect("event-list")
    return render(request , 'events/events_add.html' , {'form':form})

def addEventModel(request):
    form = EventModelForm()
    if request.method =="POST":
        form = EventModelForm(request, POST, request.FILES)
        if form.save():
         Event.objects.create(title = form.cleaned_data)
        return redirect("event-list")
    return render(request , 'events/events_add.html' , {'form':form})

def listEvent(request):
    list =Event.objects.all()
    return render (
                request,
                'events/listEvent.html',
                {'event' : list,}
            )

def detailsEvent(request ,id):
    event =Event.objects.get(id=id)
    return render (
                request,
                'events/event_detail.html',
                {'event' : event,}
            )
class EventCreatedView(CreateView):
     model = Event
     form_class = EventModelForm
     success_url=reverse_lazy('event_list')
class EventList( ListView ):
    model = Event
    template_name = "events/listEvent.html"
    context_object_name='events'
#class EventsDetails(DetailView):
    