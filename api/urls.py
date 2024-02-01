from django.urls import path,include
from .views import *
urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('addnote/', addnote),
    path('getnote/', getnote),
    path('deletenote/<id>', deletenote),
    path('updatenote/<id>', updatenote)
]