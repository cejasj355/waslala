from django.urls import path
from . import views
from django.conf import settings # Importante
from django.conf.urls.static import static # Importante
urlpatterns = [
    path("", views.index, name="index"),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<slug:slug>/', views.producto, name='producto'),
    path('login/', views.login, name='login'),
    path('carrito/', views.carrito, name='carrito'),
    path('checkout/', views.checkout, name='checkout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)