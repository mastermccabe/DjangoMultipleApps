from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def display(request):
    response = "list of users"
    # print "welcome to surveys"
    return HttpResponse(response)


def register(request):
    response = "register new user"
    return HttpResponse(response)

def login(request):
    response = "welcome to login"
    return HttpResponse(response)

def new(request):
    response = "new user"
    return HttpResponse(response)



    url(r'^$', views.display),     # This line has changed!
    # url(r'^surveys/new', views.test2),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'new$', views.new),
