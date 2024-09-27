from rest_framework import routers
from django.urls import path, include

from core.api.views import ContactUsViewSet

# default router
router = routers.DefaultRouter()

# contact us router 
router.register(r'contact_us', ContactUsViewSet, basename='contact_us')


urlpatterns = [
	path('', include((router.urls, 'core'), namespace='core'))
]