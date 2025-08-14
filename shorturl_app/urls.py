from django.urls import path
from .views import ShortUrlViewSet
from rest_framework.routers import DefaultRouter
from . views import RetrieveUrl,DeleteShortUrl,DetailShortUrl



urlpatterns = [
    path('retrieve/<str:url>', RetrieveUrl.as_view(), name='retrieve_url'),
    path('delete/<str:url>', DeleteShortUrl.as_view(), name='delete_url'),
    path('detail/<str:url>', DetailShortUrl.as_view(), name='detail_url'),
]

router = DefaultRouter()
router.register(r'', ShortUrlViewSet, basename='shorturl')
urlpatterns += router.urls