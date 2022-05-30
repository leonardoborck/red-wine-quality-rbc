from domain.CsvReader import *
from view.Menu import *
from domain.QualideDoVinhoRbc import CalculaSimilaridade

dataFrame = carregaDadosDoCsv()
dadosDoUsuario,pesosDosAtributos = CarregaPrimeiraTela()
dataFrameResultante = CalculaSimilaridade(dataFrame, dadosDoUsuario, pesosDosAtributos)

CarregaSegundaTela(dataFrameResultante,dadosDoUsuario,pesosDosAtributos)