from django.shortcuts import render

# Create your views here.
def render_chat(request):
    return render(request,'home/index2.html')
