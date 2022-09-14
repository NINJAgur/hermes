from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    return render(request,'home/main.html', context)

def record(request):
    return render(request,'home/tables-simple.html')

def calendar(request):
    return render(request,'home/calendar.html')

def contacts(request):
    return render(request,'home/examples-contacts.html')

def alerts(request):
    return render(request,'home/examples-projects.html')

def document(request):
    return render(request,'home/examples-project-add.html')

def edit(request):
    return render(request,'home/examples-project-edit.html')

def automations(request):
    return render(request,'home/index.html')

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
