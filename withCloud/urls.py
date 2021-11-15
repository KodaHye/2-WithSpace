from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views as a
from space import views as s 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a.home, name="home"),
    path('account/', include('account.urls')),
    path('space/', include('space.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)