from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView



class Home(TemplateView):       
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi carrito de compras'
        return context
    

class Response(TemplateView):       
    template_name = 'response.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'bien hecho, response'
        return context

class Success(TemplateView):       
    template_name = 'success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'bien hecho, success'
        return context