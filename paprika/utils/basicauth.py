import base64
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

def authenticated(f):
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        try:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            uname, passwd = base64.b64decode(auth[1]).split(':')
            user = authenticate(username=uname, password=passwd)
        except:
            response = HttpResponse() 
            response.status_code = 401
            response['WWW-Authenticate'] = 'Basic realm=""'
            return response

        if user is None:
            response = HttpResponse("Unauthorized")
            response.status_code = 401
            response['WWW-Authenticate'] = 'Basic realm=""'
            return response
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap
