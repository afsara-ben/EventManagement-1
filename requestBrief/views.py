from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from products.views import index
# from profile.models import user
from requestBrief.models import event_request
from .forms import requestForm
from .models import event_request

from django.contrib.auth.decorators import login_required


def request_view(request):
    form_class = requestForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = requestForm(request.POST)

    if form.is_valid():
        obj = form.save(commit=False)
        service = request.POST.getlist('service')
        # obj.service = service
        print(service)
        obj.save()
        return redirect('createBrief')

    else:
        form = requestForm()
    return render(request, 'popup.html', {'form': form}, )


def request_success(request):
    form_class = requestForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = requestForm(request.POST)

    if form.is_valid():
        obj = form.save(commit=False)
        service = request.POST.getlist('service')
        # obj.service = service
        print(service)
        obj.client_name = request.user.username
        obj.request_status = 'pending'
        obj.save()
        return redirect('createBrief')

    value = event_request.objects.latest('date_added')
    return render(request, 'popup.html', {'value': value}, )


def popup(request):
    brief = event_request.objects.all()
    context = {'brief': brief}
    # my_user = user.objects.all()
    #    return render(request, 'eventDashBoard.html', {'brief': user})
    return render(request, 'popup.html', context)


def home(request):
    return render(request, 'home.html')

