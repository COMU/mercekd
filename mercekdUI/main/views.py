# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mercekdUI.main.models import Lease, Lease_IP, Lease_Mac, LeasesFilePath
from mercekdUI.main.utils import *
import random, datetime, json

def home(request):

        count = listCount()
        context = {
           'page_title': 'Homepage',
           'count': count,
        }
	return render_to_response("home/home.html",
                            context_instance=RequestContext(request, context))

def listLeases(request, leases=0):
        if request.POST:
            q = request.POST.get('q')
            if q is not None:
                    lease_ip_list = Lease_IP.objects.filter(
                      Q(v4__contains = q) |
                      Q(ip_name__contains = q))
                    print lease_ip_list

                    lease_mac_list = Lease_Mac.objects.filter(
                        Q(mac__contains = q) |
                        Q(mac_name__contains = q))

                    print lease_mac_list

                    leases_list = Lease.objects.get_empty_query_set()
                    if len(lease_ip_list):
                        for i in lease_ip_list:
                            leases_list = leases_list | Lease.objects.filter(ip=i.id)
                    if len(lease_mac_list):
                        for i in lease_mac_list:
                            leases_list = leases_list | Lease.objects.filter(mac=i.id)
            #else:
            #    leases_list = Lease.objects.all()

        else:
            leases_list = Lease.objects.all()

        if leases == 'active':
            leases_list = parseLease(leases_list,'active')
        elif leases == 'expired':
            leases_list = parseLease(leases_list,0)
        else:
            leases_list = leases_list

        paginator = Paginator(leases_list, 50)
        if request.GET.get('page'):
            page = request.GET.get('page')
        else:
            page = 1
        try:
            leases_list = paginator.page(page)
        except PageNotAnInteger:
            leases_list = paginator.page(1)
        except EmptyPage:
            leases_list = paginator.page(paginator.num_pages)

        result = handleAliases(leases_list)

        context = {
           'page_title': 'Lease List',
           'leases_list': leases_list,
           'result': result,
           'count': listCount(),
           'now': datetime.datetime.today()
        }
	return render_to_response("home/leases.html",
                            context_instance=RequestContext(request, context))
    

def options(request):

        if request.method == 'POST':
    		file_path = request.POST['file_path']
                path = LeasesFilePath.objects.create(path = file_path)
                path.save()
 
        path_list = LeasesFilePath.objects.all()
        if path_list:
          path_list = path_list[path_list.count()-1].path
        else:
          path_list = 0
          
	context = {
           'page_title': 'Options',
           'path_file' : path_list,
	}

	return render_to_response("home/options.html",
                            context_instance=RequestContext(request, context))

@csrf_exempt
def postAlias(request):
    if request.method:
          data=json.dumps(request.POST)
          data=json.loads(data)
          post_pk = data["pk"]
          post_name = data["name"]
          post_value = data["value"]
          lease = Lease.objects.filter(id=post_pk)
          lease = lease[0]
          leases = Lease_IP.objects.filter(v4=lease.ip.v4)
          if len(leases)!=0:
              leases[0].ip_name = None
          macs = Lease_Mac.objects.filter(mac=lease.mac.mac)
          if len(macs)!=0:
              leases[0].ip_name = None
          if post_name=="mac":
            lease.mac.mac_name = post_value
            lease.mac.save()
          else:
            lease.ip.ip_name = post_value
            lease.ip.save()
    response_data={}
    response_data['result'] = 'okay'
    return HttpResponse(json.dumps(response_data), mimetype="application/json")
