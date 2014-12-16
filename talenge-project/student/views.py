from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

@login_required(login_url='/', redirect_field_name=None)
def home(request):
    context = RequestContext(request)

    context_dict = {'boldMessage': "I am bold font from the context"}

    return render_to_response('student/home.html', context_dict, context)