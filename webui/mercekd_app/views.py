from django.shortcuts import render_to_response
from django.template.context import RequestContext
from mercekd_app.models import lease_db

def home(request):
    context = dict()
    context['message'] = "Hello"
    return render_to_response("home.html",
        context_instance=RequestContext(request, context))

def anomalies(request):
    pass


def leases(request):
    ip_list=[]
    subnet_list=[]
    lease_list=lease_db.objects.all()[:5]
    for lease in lease_list:
        ip_list.append(lease.ip)
    for ip in ip_list:
        octet_firstTwo=str(ip).split(".")[0]+"."+str(ip).split(".")[1]
        octet_third=str(ip).split(".")[2]
        subnet_name=str(octet_firstTwo+"."+octet_third+".x/24")
        if subnet_name in subnet_list:
            pass
        else:
            subnet_list.append(subnet_name)
    for subnet_name in subnet_list:
        subnet_name=[]




