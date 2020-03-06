from django.urls import path
from calc import views


app_name = 'calc'
urlpatterns = [
path('home/', views.home, name= 'home'),
path('order/',views.orderForm, name = 'order'),

]
