from . import views
from django.urls import path

urlpatterns = [
    path('necklaces', views.necklaces, name='necklaces'),
    path('earrings', views.earrings, name='earrings'),
    path('rings', views.rings, name='rings')

]