# Create your views here.
import django.http

def contact(request):
    lastName = request.REQUEST["last_name"]
    return django.http.HttpResponse(lastName)
