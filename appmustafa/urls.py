from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet, UsuarioViewSet, NoticiaViewSet, ComentarioViewSet, AdopcionViewSet, CookieTokenObtainPairView, CookieTokenRefreshView, protected_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'animales', AnimalViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'adopciones', AdopcionViewSet)

urlpatterns = [
    path('token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', protected_view, name='api_protected'),
    path('', include(router.urls)),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)