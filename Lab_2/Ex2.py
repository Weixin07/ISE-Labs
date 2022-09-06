import PySimpleGUI as gui

layout = [[gui.Text("Number Addition:")],
          [gui.Text('Number 1: ',size=(20,1)), gui.Input(size=(30,1),key='no1')],
          [gui.Radio('+', "MathsOperations", enable_events=True, key='A', default=True),
          gui.Radio('-', "MathsOperations", enable_events=True, key='S'),
          gui.Radio('x', "MathsOperations", enable_events=True, key='M'),
          gui.Radio("÷", "MathsOperations", enable_events=True, key='D')],
          [gui.Text('Number 2:',size=(20,1)), gui.Input(size=(20,1),key='no2')], 
          [gui.Text('Total:',size=(20,1)), gui.Input(size=(20,1),key='total')],
          [gui.Button('Calculate'), gui.Button('Cancel')]]

winobj = gui.Window("Simple Calculator", layout)

while True:
    event, values = winobj.read()

    if event == gui.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Calculate':
        number1 = int(values['no1'])
        number2 = int(values['no2'])
        

        if values['A']:
            sumOf1n2 = number1 + number2
        elif values['S']:
            sumOf1n2 = number1 - number2
        elif values['M']:
            sumOf1n2 = number1 * number2
        elif values['D']:
            sumOf1n2 = number1 / number2
        
        winobj.Element('total').update(sumOf1n2)

