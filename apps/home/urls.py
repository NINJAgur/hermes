from django.urls import path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('primary-record', views.record, name='primary-record'),
    path('users-contacts', views.contacts, name='users-contacts'),
    path('contacts-edit/<str:user_n>', views.contacts_edit, name='contacts-edit'),
    path('users-list/', views.user_list, name='user-list'),
    path('users-del/<int:id_u>', views.user_del, name='user-list-del'),
    path('users-add/<int:id_u>', views.user_add, name='user-list-add'),
    path('users-sadd/<int:id_u>', views.user_sadd, name='user-list-sadd'),
    path('management-alerts', views.alerts, name='management-alerts'),
    path('management-document', views.alert_document, name='document'),
    path('management-manuals', views.manuals, name='manual'),
    path('management-view/<int:pk>', views.alert_view, name='management-view'),
    path('management-del/<int:pk>', views.alert_del, name='management-del'),
    path('management-edit/<int:pk>', views.alert_edit, name='management-edit'),

    path('update-del/<int:pk>/<int:id>', views.update_del, name='update-del'),
    path('manual-del/<int:pk>', views.manual_del, name='manual-del'),
    path('automations', views.automations, name='automation'),

    # re_path(r'^.*\.*', views.pages, name='pages'),
]



