# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import Q
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mercekdUI.main.models import Lease, Lease_IP, Lease_Mac, LeasesFilePath, Subnet, Status
from mercekdUI.main.utils import *
import random, datetime, json
import ipcalc
import subprocess
import os

def home(request):
        print request.LANGUAGE_CODE
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
           'current_leases': leases,
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
          try:            
           if request.POST['file_path']:
    		file_path = request.POST['file_path']
                path = LeasesFilePath.objects.create(path = file_path)
                path.save()
          except:
           pass
          try:
           if request.POST['ip'] and request.POST['mask'] and request.POST['alias']:
    		p_ip = request.POST['ip']
    		p_mask = request.POST['mask']
    		p_alias = request.POST['alias']
                p = Subnet.objects.create(ip=p_ip,mask=p_mask,alias=p_alias)
                p.save()
                l_ip = p_ip.split('.')
                l_ip = l_ip[0] + '.' + l_ip[1] + '.' + l_ip[2]
                print l_ip
                #l_id = Lease_IP.objects.filter(v4=l_ip)
                l_id =   Lease_IP.objects.filter(
                     Q(v4__contains = l_ip))
                print l_id
                for l_single in l_id:
                    print l_single.id
                    l = Lease.objects.filter(ip=l_single.id)
                    for i in l:
                        i.subnetAlias = p.alias
                        i.save()
                        print i.subnet.alias
          except:
           pass
          try:
            last_status =  list(Status.objects.all())[-1]
            pid = int(last_status.pid)
            set_status = request.POST['set_status']
            if set_status=="1":
                process = subprocess.Popen(['./bin/django', 'mercekd'])
            else:
                os.kill(pid, 9)
                last_status.status=False
                last_status.save()

          except:
              pass
        if request.method == "GET":
            try:
               d_id = request.GET['id']
               d_select = Subnet.objects.get(id=d_id)
               l_all = Lease.objects.filter(subnetAlias=d_select.alias)
               for l in l_all:
                   l.subnetAlias = "0"
                   l.save()
               d_select.delete()
            except:
               pass
 
        path_list = LeasesFilePath.objects.all()
        if path_list:
          path_list = path_list[path_list.count()-1].path
        else:
          path_list = 0
        try:
          result = Subnet.objects.all()

        except:
          pass

	context = {
           'status': list(Status.objects.all())[-1].status ,
           'page_title': 'Options',
           'path_file' : path_list,
           'count': listCount(),
           'result': result,
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

def IPv4addressmap(request):
    subnet = []
    ipv4s = []
    all_ipv4s = []
    subnets = 0
    if not request.method == "POST":
      try:
        subnets = Subnet.objects.all()
      except:
        pass
    else:
      try:
          # bu kisim relational database islemleri istiyor ancak mongodb desteklemiyor bu yuzden buraya daha iyi bir cozum bulmalisin.
          g_id = request.POST['ipv4_id']
          s_select = Subnet.objects.get(id=str(g_id))
          ipv4 = s_select.ip
          mask = s_select.mask
          alias = s_select.alias
          subnet.append(ipv4)
          subnet.append(mask)
          subnet.append(alias)
          for i in ipcalc.Network(ipv4 + '/' + mask):
              all_ipv4s.append(i)
              if Lease_IP.objects.filter(v4=i):
                #ipv4s.append(str(i).split(".")[3])
                ipv4s.append(str(i))
          subnet.append(len(all_ipv4s)-len(ipv4s))
          subnet.append(len(all_ipv4s))
          subnet.append(len(ipv4s))
      except:
          pass

    count = listCount()
    context = {
        'page_title': 'IPv4 Address Map',
        'count': count,
        'subnets': subnets,
        'subnet': subnet,
        'ipv4s': ipv4s,
        }
    return render_to_response("home/ipv4addressmap.html",
                              context_instance=RequestContext(request, context))

def getLeases(request, leases=0):
    if request.POST:
        q = request.POST.get('q')
        if q is not None:
            lease_ip_list = Lease_IP.objects.filter(
                Q(v4__contains = q) |
                Q(ip_name__contains = q))

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
    return render_to_response("home/getleases.html",
                              context_instance=RequestContext(request, context))