from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index),
    path('products',views.index),
    path('signup',views.signup)
]