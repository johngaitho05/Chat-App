from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/send_message/', consumers.ChatConsumer),
]