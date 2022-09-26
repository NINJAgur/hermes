from django.urls import path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('primary-record', views.record, name='primary-record'),
    path('primary-contacts', views.contacts, name='primary-contacts'),
    path('management-alerts', views.alerts, name='management-alerts'),
    path('management-document', views.alert_document, name='document'),
    path('management-view/<int:pk>', views.alert_view, name='management-view'),
    path('management-del/<int:pk>', views.alert_del, name='management-del'),
    path('management-edit/<int:pk>', views.alert_edit, name='management-edit'),
    path('automations', views.automations, name='automation'),

    # re_path(r'^.*\.*', views.pages, name='pages'),
]
