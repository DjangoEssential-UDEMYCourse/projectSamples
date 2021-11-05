from django.urls import path

from .views import IndexView, DadosJsonView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJsonView.as_view(), name='dados'),
]