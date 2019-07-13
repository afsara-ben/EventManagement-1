from django.urls import include, path
from .views import feedback_form


urlpatterns = [
    path('', feedback_form, name='feedback_form'),
]

