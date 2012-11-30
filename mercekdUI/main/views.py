# Create your views here.
from django.shortcuts import render_to_response
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
        addCustomLeases()
        addRandomLeases()
        result = dict()
        lease_list = Lease.objects.all()
        n=25
        paginator = Paginator(lease_list, n)
        count = listCount(lease_list)
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

        for lease in leases_list.object_list:
            ip_address = Lease_IP.objects.filter(v4=lease.ip.v4).exclude(ip_name=None)
            mac_address = Lease_Mac.objects.filter(mac=lease.mac.mac).exclude(mac_name=None)

            if len(ip_address)!=0:
                if len(mac_address)!=0:
                  result[lease] = (ip_address[0].ip_name,mac_address[0].mac_name)
                else:
                  result[lease] = (ip_address[0].ip_name,None)
            elif len(mac_address)!=0:
                  result[lease] = (None,mac_address[0].mac_name)
            else:
                  result[lease] = None


            #print result

        context = {
           'page_title': 'Homepage',
           'leases_list': leases_list,
           'result': result,
           'count': count,
        }
	return render_to_response("home/home.html",
                            context_instance=RequestContext(request, context))

def listLeases(request, leases=0):
        leases_list = Lease.objects.all()
        count = listCount(leases_list)
        result = dict()
        if leases == 'active':
          leases_list = parseLease(leases_list,'active')
        else:
          leases_list = parseLease(leases_list,0) 

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

        for lease in leases_list.object_list:
            ip_address = Lease_IP.objects.filter(v4=lease.ip.v4).exclude(ip_name=None)
            mac_address = Lease_Mac.objects.filter(mac=lease.mac.mac).exclude(mac_name=None)

            if len(ip_address)!=0:
                if len(mac_address)!=0:
                    result[lease] = (ip_address[0].ip_name,mac_address[0].mac_name)
                else:
                    result[lease] = (ip_address[0].ip_name,None)
            elif len(mac_address)!=0:
                result[lease] = (None,mac_address[0].mac_name)
            else:
                result[lease] = None




        context = {
           'page_title': 'List Leases',
           'leases_list': leases_list,
           'result': result,
           'count': count,
        }
	return render_to_response("home/home.html",
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
