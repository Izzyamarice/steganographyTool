def binaryToMessage(binary):
    try:
        count = 0
        temp = ""
        string = ""
        #converts binary string to ascii by converting in sequences of 8 bits then finding the ascii value
        for i in range(0, len(binary)):
            temp += binary[i]
            count += 1
            if count == 8:
                tempNum = int("0b"+temp,2)
                char = chr(tempNum)
                string += char
                count = 0
                temp = ""   
        return string
    except:
        print("Can't convert message")
