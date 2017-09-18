from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Welcome to surveys"
    # print "welcome to surveys"
    return HttpResponse(response)


def new(request):
    response = "hello new survey"
    return HttpResponse(response)

def edit2(request, number):
    response = number
    return HttpResponse(response)
