from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'image_form.html', {'form': form})


def success(request):
    posts = Picture.objects.all()
    return render(request, 'image_post.html', {'posts': posts})
    #return HttpResponse('successfuly uploaded')

