from django.shortcuts import render
from random import randint

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = "index.html"


class DadosJsonView(BaseLineChartView):

  def get_labels(self):
    #***retorna 12 labels para a representação do x***
    labels = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    return labels

  def get_providers(self):
    #***Retorna os Nomes dos Datasets***
    datasets = [
        "Anatomia para Escultores",
        "Gerenciamento de Projetos Com Scrum",
        "Modelagem de Veiculos Automotivos",
        "Desenvolvimento de Software com metodologia ágil",
        "Desenvolvimento de Jogos com Unreal e C#",
        "Criando APIs Moderna com Django REST Framework",
        "Criando APP com Ionic e Microserviços",
    ]
    return datasets

  def get_data(self):
    #*** Retorna 6 Datasets para plotar o grafico
    # Cada linha representa um dataset
    # Cada coluna representa um label
    # a quantidade de dados precisa ser igual aos datasets / labels
    # 12 labels entao 12 colunas
    # 6 datasets entao 6 linhas ***

    dados = []
    for l in range(6):
        for c in range(12):
            dado = [
                randint(1, 200), #jan
                randint(1, 200), #fev
                randint(1, 200), #mar
                randint(1, 200), #abr
                randint(1, 200), #mai
                randint(1, 200), #jun
                randint(1, 200), #jul
                randint(1, 200), #ago
                randint(1, 200), #set
                randint(1, 200), #out
                randint(1, 200), #nov
                randint(1, 200)  #dec
            ]
        dados.append(dado)

    return dados
