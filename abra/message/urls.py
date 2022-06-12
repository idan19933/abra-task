from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hey',views.MessageView)



urlpatterns = [
  path('',include(router.urls)),
  path('/(?P<id>.+)',include(router.urls)),


]
