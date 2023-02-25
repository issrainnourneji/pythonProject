from django.urls import path
from .views import *

urlpatterns = [
    #path('', homeEvent , name="event_home"),
    path('add/', addEvent , name="event_add"),
    #path('listStatic/', listEventStatic , name="event_list_static"),
    path('list/',listEvent , name="events_list"),
    path('listEvents/', EventList.as_view(), name="event_listC"),
    #path('details/<int:id>/', detailsEvent.as_view(), name="event_detail"),
    #path('eventsDetails/<int:pk>/', EventDetails.as_view(), name="event_Detail"),
]