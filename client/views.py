from django.shortcuts import render


def client_view(request):
    return render(request, 'client_form.html')

