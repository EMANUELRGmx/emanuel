from django.urls import path , include

from rest_framework import routers
from sales import views

router = routers.DefaultRouter()
router.register(r'sales' , views.view , 'sales')

urlpatterns = [
    path("api/v1/", include(router.urls)) ,
    
]