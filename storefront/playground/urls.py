##map url to view function

from django.urls import path  #
from . import views # from current folder ref -so that we can reference  view function

#URLCONf model -get it into main conf in storefront
urlpatterns=[
  path('hello/',views.say_hello) # always end routes with forward slash
  
 ]