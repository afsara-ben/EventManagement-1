from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset
from .forms import AgencyForm, AgencyInfoForm, AgencyBriefForm
from .models import Agency, Agency_Info, AgencyBrief


def preference_view(request):
    # try:
    #    value = AgencyBrief.objects.get(agent_username=request.user.username).order_by('id')
    #    return render(request, 'agency_form.html', {'value': value}, )
    # except AgencyBrief.DoesNotExist:
    #    value = None
    if request.method == 'POST':
        form = AgencyBriefForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.agent_username = agency_registration_username
            obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            return redirect('agency_preference_success')
    else:
        form = AgencyBriefForm()
    return render(request, 'agency_preference.html', {'form': form}, )


def preference_success(request):
    value = AgencyBrief.objects.filter(agent_username=request.user.username).order_by('-id')
    return render(request, 'agency_preference_success.html', {'value': value}, )


def agency_view(request):
    try:
        value = Agency.objects.get(agent_username=request.user.username)
        return render(request, 'agency_form.html', {'value': value}, )
    except Agency.DoesNotExist:
        value = None
        if request.method == 'POST':
            form = AgencyForm(request.POST, instance=value)

            if form.is_valid():
                obj = form.save(commit=False)
                agency_registration_username = request.user.username  # jishatech
                obj.agent_username = agency_registration_username
                obj.agent_email = request.user.email
                obj.save()
                if obj.agency_employee_number <= 10:
                    obj.agency_studio_size = "small studio"
                elif obj.agency_employee_number <= 30:
                    obj.agency_studio_size = "medium studio"
                elif obj.agency_employee_number <= 100:
                    obj.agency_studio_size = "big studio"
                elif obj.agency_employee_number > 100:
                    obj.agency_studio_size = "group"
                else:
                    obj.agency_studio_size = "i do not care"
                obj.save()
                return redirect('agency_success')
        else:
            form = AgencyForm(instance=value)
        return render(request, 'agency_form.html', {'form': form, 'value': value}, )


def agency_contact(request):
    if request.method == 'POST':
        form = AgencyInfoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.agent_username = agency_registration_username
            obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            # form.save()
            return redirect('agency_contact_success')
    else:
        form = AgencyInfoForm()
    return render(request, 'agency_contact.html', {'form': form})


def agency_success(request):
    value = Agency.objects.filter(agent_username=request.user.username).order_by('-id')[0]
    return render(request, 'agency_post.html', {'value': value}, )


def agency_contact_success(request):
    values = Agency_Info.objects.all()
    return render(request, 'agency_contact_post.html', {'values': values}, )


def edit_post(request):
    value = get_object_or_404(Agency, agent_username=request.user.username)
    if request.method == 'POST':
        form = AgencyForm(request.POST, instance=value)

        if form.is_valid():
            #  form = Agency.objects.get(agent_username=request.user.username)
            #  form.agency_company_name = request.POST['agency_company_name']
            # Agency.objects.filter(agent_username=request.user.username).update(
               # agency_company_name=request.POST['agency_company_name'],)
            # Agency.objects.filter(agent_username=request.user.username).update(
               # agency_company_website=request.POST['agency_company_website'],)
            #  form.save()
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            obj.agent_username = agency_registration_username
            obj.agent_email = request.user.email
            obj.save()
            if obj.agency_employee_number <= 10:
                obj.agency_studio_size = "small studio"
            elif obj.agency_employee_number <= 30:
                obj.agency_studio_size = "medium studio"
            elif obj.agency_employee_number <= 100:
                obj.agency_studio_size = "big studio"
            elif obj.agency_employee_number > 100:
                obj.agency_studio_size = "group"
            else:
                obj.agency_studio_size = "i do not care"
            obj.save()
            return redirect('agency_success')
    else:
        form = AgencyForm(instance=value)
    return render(request, 'agency_form.html', {'form': form, 'value': value}, )


def edit_post_contact(request):
    values = get_object_or_404(Agency_Info, agent_username=request.user.username)
    if request.method == 'POST':
        form = AgencyInfoForm(request.POST, instance=values)

        if form.is_valid():
            form = Agency_Info.objects.get(agent_username=request.user.username)
            print(request.POST.get('id'))
            form.agency_company_address = request.POST.get('agency_company_address', False)
            form.save()
            return redirect('agency_contact_success')
    else:
        form = AgencyInfoForm(instance=values)
    return render(request, 'agency_contact.html', {'form': form, 'values': values}, )

