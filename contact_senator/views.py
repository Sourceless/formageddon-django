# Create your views here.
import django.http
from lib.swartz_emailer.WriteYourRep import WriteYourRep

def contact(request):
    last_name = request.REQUEST["last_name"]
    writer = WriteYourRep()
    i = writer.prepare_i('MA-01')
    q = writer.writesenator(last_name, i)
    return django.http.HttpResponse(str(q))
