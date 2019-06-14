from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, val):
    return HttpResponse("placeholder to display number 15")

def edit(request, val):
    return HttpResponse("placeholder to edit blog" + val)

def destroy(request, val):
    return redirect("/")