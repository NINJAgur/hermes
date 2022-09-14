from django.urls import path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('primary-record', views.record, name='record'),
    path('primary-calendar', views.calendar, name='calendar'),
    path('primary-contacts', views.contacts, name='contacts'),
    path('management-alerts', views.alerts, name='alerts'),
    path('management-document', views.document, name='document'),
    path('management-edit', views.edit, name='edit'),
    path('automations', views.automations, name='automation'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]
