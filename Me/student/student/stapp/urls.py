from django.urls import path
from .import views
urlpatterns = [
    path('',views.index),
    path('',views.index,name="back"),
    path('output/',views.output,name="output"),
    path('search/',views.view,name="search"),
]