import numpy as np
from PIL import Image

def encode(srcImage, message):
    img = Image.open(srcImage, "r")
    imgArray =  np.array(img)
    width, height = img.size
    mode = img.mode
    #where i is the array number and we always want the [2] byte
    for i in range(0,len(message)):
        imgByte = imgArray[0,i,2]
        #using the fact that odd numbers have a remainder of 1 when divided by 2 so the binary would also be divisible by 2
        imgRemainder = imgByte % 2
        messageBit = message[i]
        #no code for if the imgRemainder and the messageBit are the same because it means we dont change anything
        if int(imgRemainder) == 0 and int(messageBit) == 1:
            #increase imageByte by one so that it also ends in a 1 and the message and the image match
            imgByte += 1
            imgArray[0,i,2] = np.uintc(imgByte)
        elif int(imgRemainder) == 1 and int(messageBit) == 0:
            #decrease imageByte by one so that it also ends in a 1 and the message and the image match
            imgByte -= 1         
            imgArray[0,i,2] = np.uintc(imgByte)

    #save the image as a new version, depending on the size of the file
    newImage = Image.fromarray(imgArray, mode)
    if width*height > 65500:
        try:
            newImage.save(srcImage[:-4]+"2.png")
        except:
            print("image too big")
    else:
        try:
            newImage.save(srcImage[:-4]+"2.jpg")
        except:
            print("too big")

def decode(srcImage):
    #tries to find the message text in the image and returns the message
    img = Image.open(srcImage, "r")
    imgArray = np.array(img)
    message = ""
    for i in range(0,len(imgArray)):
        imgByte = imgArray[0,i,2]  % 2
        message += str(imgByte)
    return message
