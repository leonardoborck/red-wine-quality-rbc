# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED


def PrimeiraTela():
    sg.theme('LightGrey')
    layout = [[sg.Text('Input', size=(30, 1), font='Arial', justification='center')],
              [sg.Text('Fixed Acidity', size=(12, 1)), sg.InputText(key='fixedAcidity', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='fixedAcidityCombo')],
              [sg.Text('Volatile acidity', size=(12, 1)), sg.InputText(key='volatileAcidity', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='volatileAcidityCombo')],
              [sg.Text('Citric acidity', size=(12, 1)), sg.InputText(key='citricAcidity', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='citricAcidCombo')],
              [sg.Text('Residual sugar', size=(12, 1)), sg.InputText(key='residualSugar', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='residualSugarCombo')],
              [sg.Text('Chlorides', size=(12, 1)), sg.InputText(key='chlorides', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='chloridesCombo')],
              [sg.Text('Free sulfur dioxide', size=(12, 1)), sg.InputText(key='freeSulfurDioxide', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='freeSulfurDioxideCombo')],
              [sg.Text('Total sulfur dioxide', size=(12, 1)), sg.InputText(key='totalSulfurDioxide', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='totalSulfurDioxideCombo')],
              [sg.Text('Density', size=(12, 1)), sg.InputText(key='density', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='densityCombo')],
              [sg.Text('pH', size=(12, 1)), sg.InputText(key='pH', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='pHCombo')],
              [sg.Text('Sulphates', size=(12, 1)), sg.InputText(key='sulphates', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='sulphatesCombo')],
              [sg.Text('Alcohol', size=(12, 1)), sg.InputText(key='alcohol', size=(20, 1)),
               sg.Combo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], default_value=1, size=(2, 1), key='alcoholCombo')],
              [sg.Button('Calculate', size=(15, 1), font='Arial'), sg.Button('Cancel', size=(15, 1), font='Arial')]]

    return sg.Window('Red Wine Quality', layout, finalize=True)


def CarregaPrimeiraTela():
    window = PrimeiraTela()

    while True:
        event, values = window.read()
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
                except ValueError:
                    print(f'Exceção: Valor inserido inválido.')
                    sg.popup('PUT VALID DATA!', font='Arial')

    window.close()
    return dadosDoUsuario, pesosDosAtributos


def SegundaTela():
    sg.theme('LightGrey')
    layout = [[sg.Text('Output', size=(30, 1), font='Arial', justification='center')],
              [sg.Button('Back', size=(15, 1), font='Arial'), sg.Button('Cancel', size=(15, 1), font='Arial')]]

    return sg.Window('Result', layout, finalize=True)


def CarregaSegundaTela():
    window = SegundaTela()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        elif event == 'Back':
            window.close()
            PrimeiraTela()

    window.close()

