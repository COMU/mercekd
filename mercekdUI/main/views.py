# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse


def home(request):

	context = {
		'page_title': 'Homepage'
	}

	return render_to_response("home/home.html",
                            context_instance=RequestContext(request, context))


