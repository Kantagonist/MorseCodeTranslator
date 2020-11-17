#the translation table
morseCode = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".--",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----"
}



# entry point, used for testing
if __name__ == '__main__':
    print("morseCode translator")
    entry = ""
    while(True):
        print("Translate INTO morse: (0)\nTranslate FROM morse: (1)\nexit: (2)")
        entry = input("please enter your action: ")
        if (int(entry) == 0):
            entry = input("Please input your text: ")
        #translator
        elif(int(entry) == 1):
            entry = input("Please input your morse code as a string:")
        #translator
        else:
            break;
