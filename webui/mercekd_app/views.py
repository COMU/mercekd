# Create your views here
#
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    context = dict()
    context['message'] = "Hello"
    return render_to_response("home.html",
        context_instance=RequestContext(request, context))

def anomalies(request):
    pass

def leases(request):
    pass
