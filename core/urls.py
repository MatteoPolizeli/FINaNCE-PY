from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')), #Path define a rota, e include é a Action
    path('extrato/', include('extrato.urls')),
    #cada app criado é declarado aqui,
    #aplicações em Django são dividas em 'app'
    path('planejamento/', include('planejamento.urls')),
    path('contas/', include('contas.urls'))

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
