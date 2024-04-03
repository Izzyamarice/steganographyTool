def binMessage(message):
    try:
        asciiList = []
        current = ""
        binaryStr = ""
        #this loop adds the values to one long string
        for i in range(0,len(message)):
            current = message[i]
            asciiList.append(ord(current))
            binary = ord(current)
            #to ensure that the binary version is 8 bit otherwise the decoding will not work
            binary = format(binary, '08b')
            #connects the whole binary string together
            binaryStr = str(binaryStr) + str(binary)
        return binaryStr
    except:
        return None    
