from django.template import loader

from django.http import HttpResponse

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
