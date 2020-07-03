from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
'''
class PageView(TemplateView):
    template_name = 'POST_DELETE.html'
    template_name = 'POST_FORM.html'
    template_name = 'POST_LIST.html'
'''

def form(request):
    return render(request,'POST_FORM.html')

def list(request):
    return render(request,'POST_LIST.html')

def delete(request):
    return render(request,'POST_DELETE.html')