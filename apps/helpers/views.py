from django.shortcuts import render

# Create your views here.
def error400(request, exception):
    return render(request, "handlers/page-400.html", status=400)

def error403(request, exception):
    return render(request, 'handlers/page-403.html', status=403)

def error404(request, exception):
    return render(request, 'handlers/page-404.html', status=404)

def error500(request):
    return render(request, 'handlers/page-500.html', status=500)