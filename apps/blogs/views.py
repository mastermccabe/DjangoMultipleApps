from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "Welcome to blogs"
    print "welcome to blogs"
    return HttpResponse(response)

def new(request):
    response = "hello new page"
    return HttpResponse(response)

def create(request):
    # response = "create"
    return redirect('/')
#
def show(request, number):
    response = 'blog display' + number +  '-number'
    return HttpResponse(response)
#
def edit(request, number):
    response = number
    return HttpResponse(response)

def destroy(request, number):
    response = number + ' destroyed'
    return HttpResponse(response)
