# Create your views here.


def home(request):

	context = {
		'page_title': 'Homepage'
	}

return render_to_response("home/help.html",
                            context_instance=RequestContext(request, context))


