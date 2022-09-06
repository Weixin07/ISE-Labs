import PySimpleGUI as gui
from PIL import Image, ImageTk

layout = [[gui.Text("Image Display:")],
          [gui.Image(size=(300, 300), key='-IMAGE-')],
          [gui.Button('Display'), gui.Button('Cancel')]]

winobj = gui.Window("Image Displayer", layout)

while True:
    event, values = winobj.read()

    if event == gui.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Display':
        imageDirectory = 'D:\APU Stuff\Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]\Semester 2\Imaging & Special Effects [CT029-3-2-ISE]\Mine\Labs\Lab_2\sugar.png'

        size = (300, 300)
        im = Image.open(imageDirectory)
        im = im.resize(size, resample=Image.BICUBIC)

        image = ImageTk.PhotoImage(image=im)

        winobj['-IMAGE-'].update(data=image)