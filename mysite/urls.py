
from django.contrib import admin
from django.urls import path

import agri.views

urlpatterns = [
   path("",agri.views.home),
   path("predict/",agri.views.predict)

]
