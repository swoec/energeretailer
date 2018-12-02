from django.conf.urls import url,include

from rest_framework import routers
from . import views

route = routers.DefaultRouter()
route.register(r'bill', views.BillViewSet)
route.register(r'output', views.OutputViewSet)
route.register(r'page', views.OutputPageViewSet)
route.register(r'key', views.OutputKeyViewSet)


urlpatterns = [
    url('api/', include(route.urls)),
]

urlpatterns += route.urls
