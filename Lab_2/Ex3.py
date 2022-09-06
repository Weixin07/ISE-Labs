from PIL import Image
import PySimpleGUI as gui

layout = [[gui.Text("Opening an Image:")],
          [gui.Button('Open'), gui.Button('Cancel')]]

winobj = gui.Window("Image Opener", layout)

while True:
    event, values = winobj.read()

    if event == gui.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Open':
        image = Image.open('D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_2\APULogo.png')
        image.show()
