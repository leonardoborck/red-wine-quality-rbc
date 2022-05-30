# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import PySimpleGUI as sg
import pandas as pd
from domain.CsvReader import *
from view.Menu import *
from domain.QualideDoVinhoRbc import CalculaSimilaridade
from PySimpleGUI.PySimpleGUI import WIN_CLOSED


def PrimeiraTela():
    sg.theme('LightGrey')
    layout = [[sg.Text('Input', size=(45, 1), font='Arial', justification='center')],
              [sg.Text('Fixed Acidity (4.6 - 15.9)', size=(23, 1)), sg.InputText(key='fixedAcidity', default_text='7.8' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=3, size=(2, 1), key='fixedAcidityCombo')],
              [sg.Text('Volatile acidity (0.1 - 1.6)', size=(23, 1)), sg.InputText(key='volatileAcidity', default_text='0.880' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=3, size=(2, 1), key='volatileAcidityCombo')],
              [sg.Text('Citric acidity (0.0 - 1.0)', size=(23, 1)), sg.InputText(key='citricAcidity', default_text='0' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=3, size=(2, 1), key='citricAcidCombo')],
              [sg.Text('Residual sugar (0.9 - 15.5)', size=(23, 1)), sg.InputText(key='residualSugar', default_text='2.6' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=5, size=(2, 1), key='residualSugarCombo')],
              [sg.Text('Chlorides (0.01 - 0.061)', size=(23, 1)), sg.InputText(key='chlorides', default_text='0.098' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='chloridesCombo')],
              [sg.Text('Free sulfur dioxide (1.0 - 72.0)', size=(23, 1)), sg.InputText(key='freeSulfurDioxide', default_text='25.0' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='freeSulfurDioxideCombo')],
              [sg.Text('Total sulfur dioxide (6.0 - 289.0)', size=(23, 1)), sg.InputText(key='totalSulfurDioxide', default_text='67.0' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='totalSulfurDioxideCombo')],
              [sg.Text('Density (0.990 - 1.004)', size=(23, 1)), sg.InputText(key='density', default_text='0.997' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='densityCombo')],
              [sg.Text('pH (2.7 - 4.0)', size=(23, 1)), sg.InputText(key='pH', default_text='3.2' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=6, size=(2, 1), key='pHCombo')],
              [sg.Text('Sulphates (0.3 - 2.0)', size=(23, 1)), sg.InputText(key='sulphates', default_text='0.68' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='sulphatesCombo')],
              [sg.Text('Alcohol (8.4 - 14.9)', size=(23, 1)), sg.InputText(key='alcohol', default_text='9.8' , size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=5, size=(2, 1), key='alcoholCombo')],
              [sg.Button('Calculate', size=(20, 1), font='Arial'), sg.Button('Cancel', size=(20, 1), font='Arial')]]

    return sg.Window('Red Wine Quality', layout, finalize=True)


def CarregaPrimeiraTela():
    window = PrimeiraTela()

    while True:
        event, values = window.read()
        dataFrame = carregaDadosDoCsv()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event == 'Calculate':
            if (values['fixedAcidity'] == '' or values['volatileAcidity'] == '' or values['citricAcidity'] == ''
                or values['residualSugar'] == '' or values['alcohol'] == '' or values['chlorides'] == ''
                or values['density'] == '' or values['freeSulfurDioxide'] == '' or values['totalSulfurDioxide'] == ''
                or values['pH'] == '' or values['sulphates'] == '' or float(values['fixedAcidity']) < 4.6
                or float(values['fixedAcidity']) > 15.9 or float(values['volatileAcidity']) < 0.1 or float(values['volatileAcidity']) > 1.6
                or float(values['citricAcidity']) < 0.0 or float(values['citricAcidity']) > 1.0 or float(values['residualSugar']) < 0.9
                or float(values['residualSugar']) > 15.5 or float(values['alcohol']) < 8.4 or float(values['alcohol']) > 14.9
                or float(values['chlorides']) < 0.01 or float(values['chlorides']) > 0.61 or float(values['density']) < 0.990
                or float(values['density']) > 1.004 or float(values['freeSulfurDioxide']) < 1 or float(values['freeSulfurDioxide']) > 72
                or float(values['totalSulfurDioxide']) < 6 or float(values['totalSulfurDioxide']) > 289 or float(values['pH']) < 2.7
                or float(values['pH']) > 4.0 or float(values['sulphates']) < 0.3 or float(values['sulphates']) > 2.0):
                    sg.popup('PUT VALID DATA!', font='Arial')
                    pass
                # n faz nada
                
            else:
                try:
                    fixedAcidity = float(values['fixedAcidity'])
                    volatileAcidity = float(values['volatileAcidity'])
                    citricAcidity = float(values['citricAcidity'])
                    residualSugar = float(values['residualSugar'])
                    chlorides = float(values['chlorides'])
                    freeSulfurDioxide = float(values['freeSulfurDioxide'])
                    totalSulfurDioxide = float(values['totalSulfurDioxide'])
                    density = float(values['density'])
                    pH = float(values['pH'])
                    sulphates = float(values['sulphates'])
                    alcohol = float(values['alcohol'])
                    
                    dadosDoUsuario = {
                        "fixed acidity" : fixedAcidity,
                        "volatile acidity" : volatileAcidity,
                        "citric acid" : citricAcidity,
                        "residual sugar" : residualSugar,
                        "chlorides" : chlorides,
                        "free sulfur dioxide" : freeSulfurDioxide,
                        "total sulfur dioxide" : totalSulfurDioxide,
                        "density" : density,
                        "pH" : pH,
                        "sulphates" : sulphates,
                        "alcohol" : alcohol,
                    }
                     #Entrada dos pesos do usuario
                    fixedAcidityCombo = int(values['fixedAcidityCombo'])
                    volatileAcidityCombo = int(values['volatileAcidityCombo'])
                    citricAcidityCombo = int(values['citricAcidCombo'])
                    residualSugarCombo = int(values['residualSugarCombo'])
                    chloridesCombo = int(values['chloridesCombo'])
                    freeSulfurDioxideCombo = int(values['freeSulfurDioxideCombo'])
                    totalSulfurDioxideCombo = int(values['totalSulfurDioxideCombo'])
                    densityCombo = int(values['densityCombo'])
                    pHCombo = int(values['pHCombo'])
                    sulphatesCombo = int(values['sulphatesCombo'])
                    alcoholCombo = int(values['alcoholCombo'])

                    pesosDosAtributos = {
                        "fixed acidity" : fixedAcidityCombo,
                        "volatile acidity" : volatileAcidityCombo,
                        "citric acid" : citricAcidityCombo,
                        "residual sugar" : residualSugarCombo,
                        "chlorides" : chloridesCombo,
                        "free sulfur dioxide" : freeSulfurDioxideCombo,
                        "total sulfur dioxide" : totalSulfurDioxideCombo,
                        "density" : densityCombo,
                        "pH" : pHCombo,
                        "sulphates" : sulphatesCombo,
                        "alcohol" : alcoholCombo,
                    }

                    window.close()
                    dataFrameResultante = CalculaSimilaridade(dataFrame, dadosDoUsuario, pesosDosAtributos)
                    CarregaSegundaTela(dataFrameResultante, dadosDoUsuario, pesosDosAtributos)
                except ValueError:
                    print(f'Exceção: Valor inserido inválido.')
                    sg.popup('PUT VALID DATA!', font='Arial')

    window.close()

def SegundaTela(dataFrame, dadosDoUsuario, pesosDosAtributos):
    sg.theme('LightGrey') 
    dados = pd.DataFrame([dadosDoUsuario])
    pesos = pd.DataFrame([pesosDosAtributos])
    layout = [[sg.Text('User case input:', size=(15, 1), font='Arial', justification='left'),
               sg.Table(values = dados.values.tolist(), num_rows = 1, headings = list(dados), size=(5, 1))],
              [sg.Text('Input weights:', size=(15, 1), font='Arial', justification='left'),
               sg.Table(values = pesos.values.tolist(), num_rows = 1, headings = list(pesos), size=(5, 1))],
              [sg.Text('Output:', size=(15, 1), font='Arial', justification='left')],
              [sg.Table(values = dataFrame.values.tolist(), headings = list(dataFrame), size=(5, 20))],
              [sg.Button('Back', size=(20, 1), font='Arial'), sg.Button('Cancel', size=(20, 1), font='Arial')]]

    return sg.Window('Result', layout, finalize=True)


def CarregaSegundaTela(dataFrame, dadosDoUsuario, pesosDosAtributos):
    window = SegundaTela(dataFrame, dadosDoUsuario, pesosDosAtributos)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event == 'Back':
            window.close()
            CarregaPrimeiraTela()

    window.close()

