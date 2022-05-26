import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

# Kolom Area No 1: Area open folder and select image
file_list_column = [
    [
        sg.Text("Open Image Folder :"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Choose an image from list :"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(18, 10), key="ImgList"
        )
    ],
]

# Kolom Area No 2: Area viewer image input
image_viewer_column = [
[sg.Text("Image Input :")],
[sg.Text(size=(40, 1), key="FilepathImgInput")],
[sg.Image(key="ImgInputViewer")],
]

# Kolom Area No 3: Area Image info dan Tombol list of processing
list_processing = [
    [
        sg.Text("Image Information:"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgSize"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgColorDepth"),
    ],
    [
        sg.Text("List of Processing:"),
    ],
    [
        sg.Button("Image Negative", size=(20, 1), key="ImgNegative"),
    ],
    [
        sg.Button("Image Rotate 90", size=(20, 1), key="ImgRotate90"),
    ],
    [
        sg.Button("Image Rotate 180", size=(20, 1), key="ImgRotate_180"),
    ],
    [
        sg.Button("Image Rotate 270", size=(20, 1), key="ImgRotate_270"),
    ],
    [
        sg.Button("Image Brightness Up", size=(20, 1), key="BrightnessUp"),
    ],
    [
        sg.Button("Image Brightness down", size=(20, 1), key="BrightnessDown"),
    ],
    [
        sg.Button("Image Thresholding", size=(20, 1), key="ImgThresHolding"),
    ],
    [
        sg.Button("Image Greyscale", size=(20, 1), key="ImgGreys"),
    ],
    [
        sg.Button("Image Zoom In", size=(20, 1), key="ImgZoom"),
    ],
    [
        sg.Button("Image shrinking", size=(20, 1), key="ImgZoomout"),
    ],
    [
        sg.Button("Image Flipping", size=(20, 1), key="ImgFlip"),
    ],
    [
        sg.Button("Image translasi", size=(20, 1), key="Imgtranslasi"),
    ],
    [
        sg.Button("Image median Filtering", size=(20, 1), key="Imgmedian"),
    ],
    [
        sg.Button("Image Mean Filtering", size=(20, 1), key="ImgMean"),
    ],
    [
        sg.Button("Image Erosi", size=(20, 1), key="Imgerosi"),
    ],
    [
        sg.Button("Image Dilasi", size=(20, 1), key="Imgdilasi"),
    ],
    [
        sg.Button("Image Opening", size=(20, 1), key="ImgOpening"),
    ],
    [
        sg.Button("Image Closing", size=(20, 1), key="Imgclosing"),
    ],
    [
        sg.Button("Image Blending", size=(20, 1), key="ImgBlending"),
    ],
    [
        sg.Button("Image Prewitt", size=(20, 1), key="ImgPrewitt"),
    ],
]

# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Processing Output:")],
    [sg.Text(size=(40, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
]

# Gabung Full layout
layout = [
[
    sg.Column(file_list_column),
    sg.VSeperator(),
    sg.Column(image_viewer_column),
    sg.VSeperator(),
    sg.Column(list_processing),
    sg.VSeperator(),
    sg.Column(image_viewer_column2),
    ]
]

window = sg.Window("Mini Image Editor", layout)
#nama image file temporary setiap kali processing output
filename_out = "out.png"

# Run the Event Loop
while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
# Folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]

        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]

        window["ImgList"].update(fnames)
    elif event == "ImgList": # A file was chosen from the listbox

        try:
            filename = os.path.join(
                values["ImgFolder"], values["ImgList"][0]
            )

            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            #img_input.show()

            #Size
            img_width, img_height = img_input.size
            window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height))

            #Color depth
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB":
24, "HSV": 24, "I": 32, "F": 32}
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth))
        except:
            pass
    elif event == "ImgNegative":

        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output=ImgNegative(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except: 
            pass
    elif event == "ImgRotate90":

        try:
            window["ImgProcessingType"].update("Image Rotate90")
            img_output=ImgRotate_90(img_input,coldepth,90,"C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRotate_180":

        try:
            window["ImgProcessingType"].update("Image Rotate_180")
            img_output=ImgRotate_180(img_input,coldepth,180,"C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    
    elif event == "ImgRotate_270":

        try:
            window["ImgProcessingType"].update("Image Rotate_270")
            img_output=ImgRotate_270(img_input,coldepth,270,"C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "BrightnessUp":
        
        try:
            window["ImgProcessingType"].update("BrightnessUp")
            img_output=BrightnessUp(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "BrightnessDown":
        
        try:
            window["ImgProcessingType"].update("BrightnessDown")
            img_output=BrightnessDown(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgThresHolding":
        
        try:
            window["ImgProcessingType"].update("ImgThresHolding")
            img_output=ImgThresHolding(img_input,coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgBlending":
        
        try:
            if blending == 1:
                blending=0
                window["ImgProcessingType"].update("Image Bawah")
            else:
                blending=1
                window["ImgProcessingType"].update("Image Atas")
            img_output=ImgBlending(img_input,coldepth,img2,1,1,10) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgGreys":
        
        try:
            window["ImgProcessingType"].update("ImgGreys")
            img_output=ImgGreys(img_input,coldepth) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgZoom":
        
        try:
            window["ImgProcessingType"].update("ImgZoom")
            img_output=Img_Zoom(img_input,coldepth) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgZoomout":
        
        try:
            window["ImgProcessingType"].update("ImgZoomout")
            img_output=ImgZoomout(img_input,coldepth) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlip":
        
        try:
            window["ImgProcessingType"].update("ImgFlip")
            img_output=ImgFlip(img_input,coldepth,90,"C") 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Imgtranslasi":
        
        try:
            window["ImgProcessingType"].update("Image translasi")
            img_output=Imgtranslasi(img_input,coldepth) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Imgmedian":
        
        try:
            window["ImgProcessingType"].update("image median filtering")
            img_output=Imgmedian(img_input,coldepth) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgMean":
        
        try:
            window["ImgProcessingType"].update("Img Mean filtering")
            img_output=ImgMean(img_input,coldepth) 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "Imgerosi":
        
        try:
            window["ImgProcessingType"].update("Image Erosi")
            img_output=Imgerosi(img_input,coldepth,"min") 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "Imgdilasi":
        
        try:
            window["ImgProcessingType"].update("Image Dilasi")
            img_output=Imgdilasi(img_input,coldepth,"max") 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgOpening":
        
        try:
            window["ImgProcessingType"].update("Image Opening")
            img_output=ImgOpening(img_input,coldepth,"open") 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "Imgclosing":
        
        try:
            window["ImgProcessingType"].update("Image Closing")
            img_output=ImgClosing(img_input,coldepth,"close") 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    elif event == "ImgPrewitt":
        
        try:
            window["ImgProcessingType"].update("Image Prewitt")
            img_output=ImgPrewitt(img_input,coldepth,"open") 
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
window.close()