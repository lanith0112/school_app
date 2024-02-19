from django.urls import path
from finance import views

urlpatterns = [
    path('paybill/',views.finance1),
    path('viewbill/',views.finance2),
    
]