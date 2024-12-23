from django.urls import path
from .consumers import TimerConsumer

websocket_urlpatterns = [
    path('ws/timer/',TimerConsumer.as_asgi()),
]