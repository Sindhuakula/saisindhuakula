from django.http import HttpResponse
from django.views.generic import TemplateView
"""def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")."""
class Home(TemplateView):
    template_name="index.html"

