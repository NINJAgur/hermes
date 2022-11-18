from django.shortcuts import render

# Create your views here.
def error404(request, exception):
    return render(request, 'handlers/page-404.html', status=404)