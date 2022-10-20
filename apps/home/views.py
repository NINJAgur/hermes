from datetime import datetime
import os
from turtle import update
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from . models import Manual, Record, Update
from .  import forms

@login_required(login_url="/login/")
def index(request):
    dict={
        'segment' : {'main', 'dashboard'},
        'lastestRecords'  : Record.objects.all().order_by('-id')[:6],
        'lastestUsers'   : User.objects.all().order_by('-id')[:8],
    }

    return render(request,'home/main.html', dict)

def record(request):
    records = Record.objects.all()
    context = {'main', 'record'}
    return render(request,'home/records.html', {'records': records, 'segment' : context})

def contacts(request):
    users = User.objects.all()
    context = {'main', 'contacts'}
    return render(request,'home/contacts.html', {'users': users, 'segment' : context})

def alerts(request):
    alerts = Record.objects.all()
    context = {'management', 'alerts'}
    return render(request,'home/alerts.html', {'alerts': alerts, 'segment' : context})

def alert_document(request):
    context = {'management', 'document'}

    recordForm=forms.RecordForm()
    if request.method=='POST':
        recordForm=forms.RecordForm(request.POST)
        if recordForm.is_valid():
            record=recordForm.save(commit=False)
            user=User.objects.get(id=request.POST.get('created_by'))
            record.created_by = user
            record.save()       
            messages.info(request, '!הזנת הנתונים בוצעה בהצלחה')
        else:
            print("form is invalid")
            messages.info(request, 'שגיאה בהזנת הנתונים')
        return HttpResponseRedirect('/management-alerts')
    return render(request,'home/alerts-add.html', {'recordForm':recordForm, 'segment' : context})

def alert_del(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect('/management-alerts')

def alert_edit(request, pk):
    context = {'management', 'document'}
    currentRecord = Record.objects.get(id=pk)
    recordForm=forms.RecordForm(instance=currentRecord)
    if request.method=='POST':
        recordForm=forms.RecordForm(request.POST, instance=currentRecord)
        if recordForm.is_valid():
            record=recordForm.save(commit=False)
            user=User.objects.get(id=request.POST.get('created_by'))
            record.created_by = user
            record.save()      
            messages.info(request, '!עדכון הנתונים בוצעה בהצלחה')
        else:
            print("form is invalid")
            messages.info(request, 'שגיאה בעדכון הנתונים')
        return HttpResponseRedirect('/management-alerts')
    return render(request,'home/alerts-edit.html', {'recordForm':recordForm, 'segment' : context})
    

def alert_view(request, pk):
    context = {'management', 'document'}
    record = Record.objects.get(id=pk)
    updates = Update.objects.filter(record=record)

    updateForm=forms.UpdateForm()
    if request.method=='POST':
        updateForm=forms.UpdateForm(request.POST)
        if updateForm.is_valid():
            update=updateForm.save(commit=False)
            record=Record.objects.get(id=request.POST.get('record'))
            update.record = record
            update.published = datetime.now()
            update.published_by = request.user
            update.save()      
        else:
            print("form is invalid")
        return HttpResponseRedirect('/management-view/'+str(pk))

    dict={
        'segment' : context,
        'record' : record,
        'updates' : updates,
        'updateForm': updateForm
    }

    return render(request,'home/alerts-detail.html', dict)

def update_del(request, pk, id):
    u = Update.objects.get(id=pk)
    u.delete()
    return HttpResponseRedirect('/management-view/'+str(id))

def update_del(request, pk):
    m = Manual.objects.get(id=pk)
    os.remove("apps/static/assets/upload-manuals/"+m.filename())
    m.delete()
    return HttpResponseRedirect('/management-manuals')

def manuals(request):
    context = {'management', 'document'}
    manuals = Manual.objects.all()

    manualForm=forms.ManualForm()
    if request.method=='POST':
        manualForm=forms.ManualForm(request.POST, request.FILES)
        if manualForm.is_valid():
            manual=manualForm.save(commit=False)
            manual.created_by = request.user
            manual.save()      
        else:
            print(manualForm.errors)
            messages.info(request, 'שגיאה בהזנת הנתונים')
            print("form is invalid")
        return HttpResponseRedirect('/management-manuals')

    dict={
        'segment' : context,
        'manuals': manuals,
        'manualForm': manualForm
    }

    return render(request,'home/manuals.html', dict)


def automations(request):
    context = {'automations'}
    return render(request,'home/timeline.html', {'segment' : context})

# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
