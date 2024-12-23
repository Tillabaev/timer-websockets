from django.urls import path
from .views import TimerControlView

urlpatterns = [
    path('api/timer/',TimerControlView.as_view(),name = 'timer-control'),

]
