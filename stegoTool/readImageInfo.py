import numpy as np
from PIL import Image

def encode(srcImage):
    #opens image and saves attributes + adds the pixels to the image array and returns to the original function
    try:
        img = Image.open(srcImage, "r")
        width, height = img.size
        array = np.array(list(img.getdata()))
        mode = img.mode
        if mode == "RGB":
            n =3
        elif mode == "RGBA":
            n = 4
        totalPixelNum = array.size//n
        imageInfo = [width,height,mode,n,totalPixelNum]
        return imageInfo
    except:
        return ""