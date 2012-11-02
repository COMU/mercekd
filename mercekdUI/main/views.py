# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from mercekdUI.main.models import Lease
from mercekdUI.main.utils import *
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def home(request):

        ## Adding random 100 leases to database ##
        for i in range(1,100):
           lease = Lease.objects.create(
              ip = randIP(),
              mac = randMAC(),
              starts = randDate("2012-01-21 01:01:01", "2012-06-30 11:01:59", random.random()),
              ends = randDate("2012-06-30 01:01:01", "2012-12-30 11:01:59", random.random()),
              uid = randMAC(),
              client = randName(),
           )
        ## End ##
        lease_list = Lease.objects.all()
        paginator = Paginator(lease_list, 25)
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

        context = {
           'page_title': 'Homepage',
           'leases_list': leases_list,
           'count': count,
        }
	return render_to_response("home/home.html",
                            context_instance=RequestContext(request, context))

def listLeases(request, leases=0):
        leases_list = Lease.objects.all() 
        count = listCount(leases_list)

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
    
        context = {
           'page_title': 'List Leases',
           'leases_list': leases_list,
           'count': count,
        }
	return render_to_response("home/home.html",
                            context_instance=RequestContext(request, context))
    
    
    
     
