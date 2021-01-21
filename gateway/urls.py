from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispLogReg),
    path('register', views.registerSubmit),
    path('registered', views.success),
    # need so sort of route that accepts an email address and a hash to redirect
    # to a success page
]