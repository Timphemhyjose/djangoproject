from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('You are welcome '
                        'We promise you, you will definitely like it here')