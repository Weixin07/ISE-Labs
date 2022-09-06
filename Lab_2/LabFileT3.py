import PySimpleGUI as sg

#configure the content of the window
layout = [[sg.Text("Fill in your particulars in the provided textfields")],
          [sg.Text('Name',size=(20,1)), sg.Input(size=(30,1),key='name')],
          [sg.Text('Phone No',size=(20,1)), sg.Input(size=(20,1),key='contact'), sg.Text('(010-123-4567)')],
          [sg.Text('Email Address',size=(20,1)), sg.Input(size=(100,1),key='email')],
          [sg.Text(size=(100,3), key='feedback')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

# Create the Window
winobj = sg.Window("User Registration", layout)

# User interaction
while True:
    event, values = winobj.read()
    # when user click close
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    # system response on window
    winobj['feedback'].update('Thank you '+ values['name'] + ' for registring with us. \n An email will be sent to your mailbox at '+ values['email'])

# Close the window
winobjx.close()
