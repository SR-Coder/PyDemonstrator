from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dispLogReg),
    path('register', views.registerSubmit),
    path('registered', views.success),

    path('pda', views.displayAdminPage),
    # need so sort of route that accepts an email address and a hash to redirect
    # to a success page

    # AJAX Routes
    path('users',views.dispUsers, name='users'),
]