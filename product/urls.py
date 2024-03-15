from django.urls import path
from .views import index,contact,shop,why,testmon,base
urlpatterns = [
    path('',index,name="home"),
    path('contact',contact,name="contact"),
    path('shop',shop,name='shop'),
    path('why',why,name='why'),
    path('testmonial',testmon,name='tesmonial')
]
