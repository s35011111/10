from django.urls import include, path
from rest_framework.routers import DefaultRouter

#from config.urls import urlpatterns
from page.views import PageViewSet

router=DefaultRouter()
router.register(r'page',PageViewSet,basename='page')#

urlpatterns=[
    path('',include(router.urls)),
   # path('register/',RegisterView.as_view(), name='register'),
]