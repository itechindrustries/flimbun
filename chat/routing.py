# chat/routing.py
from django.urls import re_path

from . import consumers

# (?P<room_name>\w+)/$
# (?P<room_name>[0-9a-f-]+)

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>[0-9a-f-]+)/$', consumers.ChatConsumer),
]