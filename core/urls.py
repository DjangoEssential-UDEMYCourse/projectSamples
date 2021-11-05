from django.urls import path

from .views import IndexView, DadosJsonView, RelatorioPDFView, Relatorio2View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('charts/', IndexView.as_view(), name='charts'),
    path('dados/', DadosJsonView.as_view(), name='dados'),
    path('relatorio/', RelatorioPDFView.as_view(), name='relatorio'),
    path('relatorio2/', Relatorio2View.as_view(), name='relatorio-wp'),
]