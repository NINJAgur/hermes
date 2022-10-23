from django.urls import path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('primary-record', views.record, name='primary-record'),
    path('primary-contacts', views.contacts, name='primary-contacts'),
    path('user_list/', views.user_list, name='user_list'),
    path('users-del/<int:id_u>', views.user_del, name='user_list-del'),
    path('users-add/<int:id_u>', views.user_add, name='user_list-add'),
    path('users-sadd/<int:id_u>', views.user_sadd, name='user_list-sadd'),
    path('management-alerts', views.alerts, name='management-alerts'),
    path('management-document', views.alert_document, name='document'),
    path('management-info', views.alert_info, name='info'),
    path('management-view/<int:pk>', views.alert_view, name='management-view'),
    path('management-del/<int:pk>', views.alert_del, name='management-del'),
    path('management-edit/<int:pk>', views.alert_edit, name='management-edit'),

    path('update-del/<int:pk>/<int:id>', views.update_del, name='update-del'),
    path('automations', views.automations, name='automation'),

    # re_path(r'^.*\.*', views.pages, name='pages'),
]



