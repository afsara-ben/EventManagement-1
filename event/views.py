
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# Create your views here.
from event.models import Event


# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'event_list'
    template_name = 'event/index.html'

    def get_queryset(self):
        return Event.objects.all()


# view for the event entry page
class EventEntry(CreateView):
    model = Event
    # the fields mentioned below become the entry rows in the generated form
    fields = ['event_name', 'event_venue', 'event_type']


# view for the event update page
class EventUpdate(UpdateView):
    model = Event
    # the fields mentioned beindexlow become the entyr rows in the update form
    fields = ['event_name', 'event_venue', 'event_type']


# view for deleting a event entry
class EventDelete(DeleteView):
    model = Event
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('event:index')