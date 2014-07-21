# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import os

from rango.models import Category
from rango.models import Page
from rango.admin import Category

import tango_with_django_project.settings as SETTINGS
import xml.etree.cElementTree as etree

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query for categories - add the list to our context dictionary.
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.all().order_by('-views').reverse()[:999]
    context_dict = {'categories': category_list,
                    'pages': pages_list
                   }

    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for category in category_list:
        category.url = category.name.replace(' ', '_')

    # Render the response and return to the client.
    return render_to_response('rango/index.html', context_dict, context)

### test
def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/about.html', context_dict, context)

def category(request, category_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    category_name = category_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'category_name': category_name}

    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('rango/category.html', context_dict, context)

def code_coverage(request):
    delete_file()
    context = RequestContext(request)
    tree = etree.parse("{0}/rango/logs/clover.xml".format(SETTINGS.PROJECT_PATH))
    root = tree.getroot()
    metric = root[0][0]
    
    metrics_list = []
    metrics_list.append({"statements":metric.get('statements'),"coveredstatements":metric.get('coveredstatements')})

    context_dict = {'metrics_list': metrics_list}
    return render_to_response('rango/code_coverage.html', context_dict, context)

# helper method for code_coverage view
def delete_file():
    files = os.listdir("{0}/rango/logs/".format(SETTINGS.PROJECT_PATH))
    if files.count < 10:
        return
    os.remove("{0}/rango/logs/{1}".format(SETTINGS.PROJECT_PATH, files[0]))