from django.urls import path
from main.views import *

urlpatterns = [
    path('',index,name='index'),
    path('ru/',ru,name='ru'),
    path('uz/',uz,name='uz'),
]