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
       sg.Text("Select another Image for Merge"),
       sg.In(size=(25, 1), enable_events=True, key="-FILE2-"),
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
       sg.Radio('RGB Color', "RADIO1",default=False, key="-UserOptR-"),
       sg.Radio('Merge with Colours', "RADIO1",default=False, key="-UserOptM-")
    ]
]

seg2 = [
    [sg.Text("OUTPUT")],
    [sg.Text("Selected Image:"),sg.Text(size=(40, 1), key="-SELECTFILE-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Text("Selected Image for Merge:"),sg.Text(size=(40, 1), key="-SELECTFILE2-")],
    [sg.Image(key="-IMAGE2-")],
    [sg.Text("Merged Image:"),sg.Text(size=(40, 1), key="-M-")],
    [sg.Image(key="-IMAGE3-")],
]
layout = [
    [
        sg.Column(seg1),
        sg.VSeperator(),
        sg.Column(seg2),
    ]
]

wind = sg.Window("My Application", layout,size=(800, 800)) #.read()

while True:
    event, values = wind.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break
    
    if event == "Load Image":
            filename = values["-FILE-"]
            filename2 = values["-FILE2-"]

            if os.path.exists(filename):
                wind["-SELECTFILE-"].update(filename)
                image = Image.open(filename)
                image.thumbnail((400, 400))
                
                wind["-SELECTFILE2-"].update(filename2)
                image2 = Image.open(filename2)
                image2.thumbnail((400, 400))
                
                image3 = Image.open("D:/APU Stuff/Bachelor of Computer Science (Intelligent Systems) [APD2F2202CS(IS)]/Semester 2/Imaging & Special Effects [CT029-3-2-ISE]/Mine/Labs/ISE-Labs/Lab_10/NOTSELECTED.png")
                image3.thumbnail((400, 400))

                if values["-UserOptB-"] == True:
                    image = image.convert("1")
                elif values["-UserOptG-"] == True:
                    image = image.convert("L")
                elif values["-UserOptR-"] == True:
                    image = image.convert("RGB")
                else:
                    resizedImage2=image2.resize((image.width, image.height))
                    
                    image.putalpha(100)
                    resizedImage2.putalpha(150)
                    image3 = Image.alpha_composite(resizedImage2,image)

                photo_img = ImageTk.PhotoImage(image)      
                wind["-IMAGE-"].update(data=photo_img)
                photo_img2 = ImageTk.PhotoImage(image2)      
                wind["-IMAGE2-"].update(data=photo_img2)
                photo_img3 = ImageTk.PhotoImage(image3)      
                wind["-IMAGE3-"].update(data=photo_img3)

wind.close()
