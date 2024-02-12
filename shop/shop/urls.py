"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from product.views import Taskviewsets,Employeedetails,Employeeinfo
from product import views
from django.conf import settings

router = routers.SimpleRouter()
router.register('Task',Taskviewsets)
router.register('Dueview',views.Dueviewsets)
router.register('Completeview',views.Completedviewsets)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('emp',Employeedetails.as_view(),name='emp'),
    path('emp/<int:id>/',Employeeinfo.as_view(),name='emp')
]
