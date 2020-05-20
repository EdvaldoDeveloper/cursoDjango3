from django.http import HttpResponse

def hello_world(requist):
    return HttpResponse('Hello World')