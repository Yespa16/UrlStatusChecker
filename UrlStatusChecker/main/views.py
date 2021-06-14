from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Url
from django.views.generic import ListView 
# Create your views here.

def home(request):
    # User authentication is checked here not in front-end (as said in task)
    if request.user.is_authenticated:
        urls = Url.objects.all()
        return render(request, "main/home.html", {"urls": urls})
    else:
        return HttpResponse("Please Authenticate to see urls and their response")


def check_url(request, link):
    try:
        url = Url.objects.get(link=link)
        return JsonResponse(url.status_code, safe=False)
    except:
        return JsonResponse("Link does not exist in database", status=404, safe=False)