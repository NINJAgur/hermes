from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import User
from apps.authentication import models

#@login_required(login_url="/login/")
def user_list(request):
    u = models.CustomUser.objects.filter(active=False)
    active_user = models.CustomUser.objects.filter(active=True)
    for user in u:
        print(user.active)
        if request.POST.get(user.name) == "add":
            user.active = True
            user.save()
            
            
        else:
            if request.POST.get(user.name) == "delete":
                delete_user = models.CustomUser.objects.get(name=user.name)
                delete_user.delete()
                
    for user in active_user:
        if request.POST.get(user.name) == "delete":
            delete_user = models.CustomUser.objects.get(name=user.name)
            delete_user.delete()
        
    return render(request, "home/user_list.html", {"u":u, "active_user":active_user})

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    return render(request,'home/main.html', context)

def record(request):
    users = User.objects.all()
    return render(request,'home/records.html', {'users': users})

def contacts(request):
    return render(request,'home/contacts.html')

def alerts(request):
    return render(request,'home/examples-projects.html')

def document(request):
    return render(request,'home/examples-project-add.html')

def edit(request):
    return render(request,'home/examples-project-edit.html')

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
