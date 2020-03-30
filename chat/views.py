from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json
from django.contrib import messages
import uuid
from django.contrib.auth.models import User
from .models import *

# messages.success(request, 'Your Settings was successfully updated!')
# Create your views here.
def home(request):
    title = "Flimbun"
    di ={'title':title}
    group = Group.objects.filter(user= request.user)
    di['group'] = group
    if request.method == 'POST':
        if request.POST['post'] == 'create-group':
            try:
                title = request.POST['new-chat-title']
                topic = request.POST['new-chat-topic']
                description = request.POST['new-chat-description']
                friends = request.POST.getlist('checks[]')
                friends.append(request.user.username)
                if len(friends)<3:
                    messages.error(request, 'At least 3 members required in a group')
                    return HttpResponseRedirect(reverse('index'))
                grp_url=uuid.uuid5(uuid.NAMESPACE_DNS, f'{title}{request.user.username}')
                new_grp = Group(group_url=grp_url,name=title,topic=topic,description=description)
                new_grp.save()
                for i in friends:
                    usr = User.objects.get(username = i)
                    new_grp.user.add(usr)
                messages.success(request, f'New group {title} created')
            except expression as e:
                messages.error(request, e)
  
    return render(request, 'index.html',di )

@login_required
def room(request, room_name):
    title = "Flimbun"
    room_name = str(room_name)
    di ={'title':title,'room_name': room_name,'title':'Chat Room '+room_name,
        'username': request.user.username}
    group = Group.objects.filter(user= request.user)
    di['group'] = group
    return render(request, 'chat.html', di)
