def CalculaSimilaridade(dataFrame, dadosDoUsuario, pesosDosAtributos):
    dataFrame['Similaridade'] = 0.0
    for linha in range(len(dataFrame)):
        dataFrame['Similaridade'][linha] = CalculaSimilaridadeDoCaso(dataFrame, dadosDoUsuario, pesosDosAtributos, linha)
    
    return dataFrame.sort_values(by='Similaridade', ascending=False)
    
def CalculaSimilaridadeDoCaso(dataFrame, dadosDoUsuario, pesosDosAtributos, linha):
    similaridade = CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'fixed acidity') * pesosDosAtributos['fixed acidity']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'volatile acidity') * pesosDosAtributos['volatile acidity']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'citric acid') * pesosDosAtributos['citric acid']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'residual sugar') * pesosDosAtributos['residual sugar']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'chlorides') * pesosDosAtributos['chlorides']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'free sulfur dioxide') * pesosDosAtributos['free sulfur dioxide']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'total sulfur dioxide') * pesosDosAtributos['total sulfur dioxide']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'density') * pesosDosAtributos['density']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'pH') * pesosDosAtributos['pH']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'sulphates') * pesosDosAtributos['sulphates']
    similaridade += CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, 'alcohol') * pesosDosAtributos['alcohol']
    similaridade = similaridade / SomaDosPesosDosAtributos(pesosDosAtributos)
    
    return similaridade
    
def SomaDosPesosDosAtributos(pesosDosAtributos):
    somaDosPesos = 0
    for peso in pesosDosAtributos.values():
        somaDosPesos += peso
    
    return somaDosPesos

def CalculaSimilaridadeDoAtributo(dataFrame, dadosDoUsuario, linha, coluna):
    dadoDaBase = dataFrame[coluna][linha]
    dadoDoUsuario = dadosDoUsuario[coluna]
    similaridadeDoAtributo = 1 - (abs(dadoDaBase - dadoDoUsuario)/CalculaAmplitude(coluna))
    
    return similaridadeDoAtributo

def CalculaAmplitude(atributo):
    if(atributo == "fixed acidity"):
        return 11.3
    if(atributo == "volatile acidity"):
        return 1.5
    if(atributo == "citric acid"):
        return 1.0
    if(atributo == "residual sugar"):
        return 14.6
    if(atributo == "chlorides"):
        return 0.6
    if(atributo == "free sulfur dioxide"):
        return 71.0
    if(atributo == "total sulfur dioxide"):
        return 283.0
    if(atributo == "density"):
        return 0.014
    if(atributo == "pH"):
        return 1.3
    if(atributo == "sulphates"):
        return 1.7
    return 6.5 #alcohol