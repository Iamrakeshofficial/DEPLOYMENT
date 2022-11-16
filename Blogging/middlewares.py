# This is Proces Based MiddleWares.
from django.shortcuts import HttpResponse,render
class Process:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        response=render(request,'site.html')
        return response

