from django.urls import path
from . import views

urlpatterns = [
    path('yieldprediction',views.yieldprediction,name='yieldprediction'),
    path('cropprediction',views.cropprediction,name='cropprediction'),
]