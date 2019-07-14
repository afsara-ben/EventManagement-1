"""eventManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from reg_group.views import client, agency, reg_group, vendor
from requestBrief.views import popup, request_view
from requestBrief.views import request_success, match, match_success
from relation.views import AdSearchView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reg_group.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', reg_group.SignUpView.as_view(), name='signup'),
    path('accounts/signup/client/', client.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/signup/agency/', agency.AgencySignUpView.as_view(), name='agency_signup'),
    path('accounts/signup/vendor/', vendor.VendorSignUpView.as_view(), name='vendor_signup'),
    path('search/', agency.SearchResultsView.as_view(), name='search_results'),
    path('myrequest/', request_view, name='popup'),
    path('myBrief/', request_success, name='createBrief'),
    path('mymatch/', match, name='mymatch'),
    path('mymatch/agency/', match_success, name='agency_match'),
    path('agency/search/', AdSearchView.as_view(), name='search'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('feedback/', include('feedback.urls')),

    url(r'^event/', include('event.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
