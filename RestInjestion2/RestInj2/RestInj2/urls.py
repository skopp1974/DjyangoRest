"""RestInj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#from django.urls import path
#from RigApp.views import rig_list, rig_detail, rig_home

#urlpatterns = [
#     path('', rig_home, name="rig_home"),
#     path('admin/', admin.site.urls),
#     path("rigs/", rig_list, name="rig_list"),
#     path("rigs/<int:pk>/", rig_detail, name="rig_detail")
# ]
from django.contrib import admin
from django.urls import path
from RigApp.apiviews import RigList, RigDetail
from RigApp.views import rig_home

urlpatterns = [
    path("rigs/", RigList.as_view(), name="rig_list"),
    path("rigs/<int:pk>/", RigDetail.as_view(), name="rig_detail"),
    path('admin/', admin.site.urls),
    path('', rig_home, name="rig_home"),
]

