from django.http import HttpResponse

# first view from the django documentation
def index(request):
    return HttpResponse("Hello, world. You're at the core index.")