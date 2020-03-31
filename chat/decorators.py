from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

def user_handelaar(function):
    def _inner(request,room_name, *args, **kwargs):
        try:
            try:
                print(fchat.objects.filter(fuser= request.user,furl=room_name).first().fuser.all())
            except:
                print(Group.objects.filter(group_url= room_name,user= request.user).first().user.all())
        except:
            return HttpResponseRedirect(reverse('index'))
        return function(request,room_name, *args, **kwargs)
    return _inner