#the translation table
morseCode = {
    "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....",
    "I" : "..", "J" : ".--", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.",
    "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-",
    "Y" : "-.--", "Z" : "--..","a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.",
    "g" : "--.", "h" : "....", "i" : "..", "j" : ".--", "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.",
    "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-",
    "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..",
    "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...",
    "8" : "---..", "9" : "----.", "0" : "-----"
}
reverseMorseCode = {
    ".-" : "A", "-..." : "B", "-.-." : "C", "-.." : "D", "." : "E", "..-." : "F", "--." : "G", "...." : "H",
    ".." : "I", ".--" : "J", "-.-" : "K", ".-.." : "L", "--" : "M" , "-." : "N", "---" : "O", ".--." : "P",
    "--.-" : "Q", ".-." : "R", "..." : "S", "-" : "T", "..-" : "U", "...-": "V", ".--" : "W", "-..-" : "X",
    "-.--" : "Y", "--.." : "Z",
    ".----" : "1", "..---" : "2", "...--" : "3", "....-" : "4", "....." : "5", "-...." : "6", "--..." : "7",
    "---.." : "8", "----." : "9", "-----" : "0"
}

#has two modes:
# 0: translate into morse
# 1: translate a morse code into text
class MorseTranslator:
    def __init__(self, mode):
        self.mode = mode
    def translate(self, text):
        result = ""
        if self.mode == 0:
            #cleanig the input
            refinedEntry = ""
            for i in text:
                if i in morseCode:
                    refinedEntry += i
            #translate
            for i in refinedEntry:
                result += "" + morseCode.get(i) + " "
        elif self.mode == 1:
            #splits the input via free spaces
            refinedEntry = text.split()
            for i in refinedEntry:
                if i in reverseMorseCode:
                    result += reverseMorseCode.get(i)
        return result


# entry point, used for testing
if __name__ == '__main__':
    print("morseCode translator")
    entry = ""
    while(True):
        print("Translate INTO morse: (0)\nTranslate FROM morse: (1)\nexit: (2)")
        entry = input("please enter your action: ")
        if (int(entry) == 0):
            entry = input("Please input your text: ")
            t = MorseTranslator(0)
            print("your output: " + t.translate(entry))
        elif(int(entry) == 1):
            entry = input("Please input your morse code as a string:")
            t = MorseTranslator(1)
            print("your output:" + t.translate(entry))
        else:
            break;
