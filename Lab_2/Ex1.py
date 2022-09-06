import PySimpleGUI as gui

layout = [[gui.Text("Number Addition:")],
          [gui.Text('Number 1: ',size=(20,1)), gui.Input(size=(30,1),key='no1')],
          [gui.Text('Number 2:',size=(20,1)), gui.Input(size=(20,1),key='no2')], 
          [gui.Text('Total:',size=(20,1)), gui.Input(size=(20,1),key='total')],
          [gui.Button('Add'), gui.Button('Cancel')]]

winobj = gui.Window("User Registration", layout)

while True:
    event, values = winobj.read()

    if event == gui.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Add':
        number1 = int(values['no1'])
        number2 = int(values['no2'])
        sumOf1n2 = number1 + number2
        winobj.Element('total').update(sumOf1n2)

