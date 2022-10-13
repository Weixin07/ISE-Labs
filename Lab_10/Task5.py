import PySimpleGUI as sg
import os.path
from PIL import Image, ImageTk

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
seg1 = [
    [
       sg.Text("Select an Image"),
       sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
       sg.FileBrowse()
    ],
    [
        sg.Button("Load Image")
    ],
    [
        sg.Text("Select an Operation:\n")
    ],
    [
       sg.Radio('Black and White', "RADIO1", default=False, key="-UserOptB-"),
       sg.Radio('GrayScale Color', "RADIO1",default=True, key="-UserOptG-"),  
       sg.Radio('RGB Color', "RADIO1",default=False, key="-UserOptR-")
    ]
]

seg2 = [
    [sg.Text("OUTPUT")],
    [sg.Text("Selected Image:"),sg.Text(size=(40, 1), key="-SELECTFILE-")],
    [sg.Image(key="-IMAGE-")],
]
layout = [
    [
        sg.Column(seg1),
        sg.VSeperator(),
        sg.Column(seg2),
    ]
]

wind = sg.Window("my Application", layout,size=(800, 400)) #.read()

while True:
    event, values = wind.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break
    
    if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                wind["-SELECTFILE-"].update(filename)
                image = Image.open(filename)
                image.thumbnail((400, 400))
              
                if values["-UserOptB-"] == True:
                    image = image.convert("1")
                elif values["-UserOptG-"] == True:
                    image = image.convert("L")
                else:
                    image = image.convert("RGB")

                photo_img = ImageTk.PhotoImage(image)      
                wind["-IMAGE-"].update(data=photo_img)

wind.close()
