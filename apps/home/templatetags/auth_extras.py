from django import template
from django.contrib.auth.models import Group, User
from apps.home.models import Record
from apps.chat.models import Room
import datetime

register = template.Library()

lastestAlerts = Record.objects.filter(date_start=datetime.date.today()).count()
latestMessages = Room.objects.filter(updated=datetime.date.today()).count()
latestUserSignUp = User.objects.filter(date_joined=datetime.date.today()).count()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

@register.filter(name='get_alerts')
def get_alerts(user):
    return lastestAlerts

@register.filter(name='get_messages')
def get_messages(user):
    return latestMessages

@register.filter(name='get_users')
def get_users(user):
    return latestUserSignUp

@register.filter(name='get_notifications')
def get_notifications(user):
    return latestUserSignUp + lastestAlerts