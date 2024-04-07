import readImageInfo as rII
import convertMessageToBin as cmTb
import convertBinToMessage as cbTm
import manipulateImage as MI


class StegoExecution():
    def __init__(self):
        self._imgName = ''
        self._width = ''
        self._height = ''
        self._mode = ''
        self._n = ''
        self._totalPixelnum = ''
        self._message = ''
        self._encodedMessage = ''

    #sets all the attributes for the image in use
    def setImgDetails(self,srcImage):
        try:
            self._imgName =  srcImage
            imageInfo = rII.encode(srcImage)
            self._width = imageInfo[0]
            self._height = imageInfo[1]
            self._mode = imageInfo[2]
            self._n = imageInfo[3]
            self._totalPixelnum = imageInfo[4]
        except:
            print("Invalid image")
    
    #checking to see if there are enough pixels for the message
    def checkImageLength(self):
        try:
            if int(self._totalPixelnum) < len(self._message):
                return False
            else:
                return True
        except ValueError as e:
            print(e)
            return False

    #if the message they enter is in the small chance the same as the delimiter, then return False since this mustn't be true
    def checkMessage(self):
        if self._message == "$ENDOFMESSAGE$":
            return False
        else:
            return True

    def encodeImage(self):
        #follows encoding image code - output is the new file
        try:
            print("encoding the image")
            MI.encode(self._imgName,self._encodedMessage)
        except:
            print("Image cannot undergo this tool")

    def decodeImage(self):
        #follows the decodeImage code - saves the message picked up into the encodedMessage attribute
        try:
            self._encodedMessage = MI.decode(self._imgName)
        except:
            print("Image cannot undergo this tool")

    def setMessage(self,message):
        #sets the message that the user wants to be in the image
        self._message = message

    def encodeMessage(self):
        #encodes message from ascii to binary
        self._encodedMessage = cmTb.binMessage(self._message)

    def decodeMessage(self):
        #decodes message from binary to ascii
        self._message = cbTm.binaryToMessage(self._encodedMessage)

    def getMessage(self):
        #checks first if delimiter is definitely in the message - if not then it won't attempt to further decode the message
        delim = "$ENDOFMESSAGE$"
        if delim in self._message:
            self._message = self._message.split("$ENDOFMESSAGE$")[0]
            return self._message
        else:
            return None


def decode(imgPath):
    file = StegoExecution()
    #sets all the details for their chosen message and then decodes it
    file.setImgDetails(imgPath)
    file.decodeImage()
    #decodes the message into ascii
    file.decodeMessage()
    #attempts to find the delimiter in the output and removes everything after this
    message = file.getMessage()
    return message

def encode(imgPath,msg):
    file = StegoExecution()
    #sets the user message
    message = msg + "$ENDOFMESSAGE$"
    print(message)
    #set the message inside the object variable and convert to binary
    file.setMessage(message)
    #check if the message = the delimiter
    valid = file.checkMessage()
    if valid == False:
        print("This is not allowed")
    else:
        file.encodeMessage()
    image = imgPath
    file.setImgDetails(image)
    #check if there are enough bits
    valid = file.checkImageLength()
    if valid == False:
        print("This is not allowed")
    else:
        file.encodeImage()


