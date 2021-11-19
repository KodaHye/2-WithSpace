from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from space import views as space

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', space.firstpage, name='firstpage'),
    path('account/', include('account.urls')),
    path('space/', include('space.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)