from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from . models import Record
from django.http import HttpResponseRedirect

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    return render(request,'home/main.html', context)

def record(request):
    records = Record.objects.all()
    return render(request,'home/records.html', {'records': records})

def contacts(request):
    users = User.objects.all()
    return render(request,'home/contacts.html', {'users': users})

def alerts(request):
    alerts = Record.objects.all()
    return render(request,'home/alerts.html', {'alerts': alerts})

def alert_document(request):
    return render(request,'home/alerts-add.html')

def alert_del(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return HttpResponseRedirect('/management-alerts')

def alert_edit(request, pk):
    return render(request,'home/alerts-edit.html')

def alert_view(request, pk):
    return render(request,'home/alerts-detail.html')

def automations(request):
    return render(request,'home/timeline.html')

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
