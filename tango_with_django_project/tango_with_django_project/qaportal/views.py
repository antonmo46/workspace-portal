from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

import os
import tango_with_django_project.settings as SETTINGS
import xml.etree.cElementTree as etree

# Create your views here.
def index(request):
    delete_file()
    context = RequestContext(request)
    tree = etree.parse("{0}/qaportal/logs/clover.xml".format(SETTINGS.PROJECT_PATH))
    root = tree.getroot()
    metric = root[0][0]
    
    metrics_list = []
    metrics_list.append({"statements":metric.get('statements'),"coveredstatements":metric.get('coveredstatements')})

    context_dict = {'metrics_list': metrics_list}
    return render_to_response('qaportal/index1.html', context_dict, context)

# helper method for code_coverage view
def delete_file():
    files = os.listdir("{0}/qaportal/logs/".format(SETTINGS.PROJECT_PATH))
    #if files.count < 10:
    #    return
    #os.remove("{0}/qaportal/logs/{1}".format(SETTINGS.PROJECT_PATH, files[0]))
