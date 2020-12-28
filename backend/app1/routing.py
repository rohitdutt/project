# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    #re_path(r'ws/chat/(?P<userName>\w+)/$',consumers.ChatConsumer.as_asgi()),
   re_path(r'^ws/chat/(?P<userName>\w+)/$',consumers.ChatConsumer.as_asgi()),
    #re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),

    #re_path(r'^ws/chat/(?Pmyroom\w+)/b/$',consumers.privatchat.as_asgi()),
    #re_path(r'ws/chat/1o1$',consumers.ChatConsumer.as_asgi()),
]
#.as_asgi()
