from itertools import chain

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from products.views import index
# from profile.models import user
from requestBrief.forms import requestForm
from requestBrief.models import event_request
from agency.models import AgencyBrief, Agency_Info, Agency


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
        obj.client_name = request.user.username
        obj.request_status = 'pending'
        print(service)
        obj.save()
    #    return redirect('createBrief')
        return redirect('mymatch')

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
    #    return redirect('createBrief')
        return redirect('mymatch')

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


def match(request):
    count = 0
    value = event_request.objects.latest('date_added')
    agency_brief_match = AgencyBrief.objects.filter((Q(agency_specialty__icontains=value.service) |
                                             Q(agency_interest__icontains=value.service)) &
                                             Q(agency_remote_work__icontains=value.client_remote_work) &
                                             Q(agency_event_budget__icontains=value.range))

    count = 40

    if value.client_remote_work is "no":
        agency_info_match = Agency_Info.objects.filter(Q(agency_company_address__icontains=value.location))
        count = 60
    else:
        agency_info_match = Agency_Info.objects.filter(Q(agency_company_address__icontains=value.location) |
                                                       ~Q(agency_company_address__icontains=value.location))
        count = 50

    if value.size != "I do not care":
        agency_match = Agency.objects.filter(Q(agency_language__icontains=value.language) &
                                             Q(agency_studio_size__icontains=value.size))
        count = count + 20
    else:
        agency_match = Agency.objects.filter(Q(agency_language__icontains=value.language))
        count = count + 10

    result_list = sorted(chain(agency_brief_match,
                               agency_match,
                               agency_info_match,
                               ),
                         key=lambda instance: instance.date_added)

    print(value.range)
    sku = "jishacompany"
    context = {
        'value': value,
        'result_list': result_list,
        'count': count,
        'agency_brief_match': agency_brief_match,
        'agency_match': agency_match,
        'agency_info_match': agency_info_match,
        'sku': sku,
    }
    return render(request, 'popup.html', context, )


def match_success(request):
    if request.method == 'GET':
        sku = request.GET.get('sku')
        if not sku:
            return render(request, 'popup.html')
        else:
            message = "hello"
            agency_detail = Agency.objects.get(agency_company_name=sku)
            context = {
                'sku': sku,
                'message': message,
                'agency_detail': agency_detail,
            }
            return render(request, 'agency_match.html', context)

