from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('api/category/', include('apps.category.urls')),
    path('api/product/', include('apps.product.urls')),
    path('api/cart/', include('apps.cart.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Incluye tus otras rutas de Django aquí, por ejemplo:
    # path('api/', include('your_app.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]