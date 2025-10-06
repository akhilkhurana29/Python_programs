morse_code = {
    # Letters
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",  
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",  
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",  
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",  

    # Punctuation
    ".": ".-.-.-",  ",": "--..--",  "?": "..--..",  "'": ".----.",  
    "/": "-..-.",   ":": "---...",  ";": "-.-.-.",  "=": "-...-",  
    "+": ".-.-.",   "-": "-....-",  "\"": ".-..-.", 
}


# string = input("enter the string you want to convert:")
def text_to_morsecode(string):
    empty_string = ""
    # for char in string:
    #     print(char)
    #     for key,value in morse_code.items():
    #         if char.upper() == key:
    #             empty_string += f"{value} "
    # print(empty_string)

    for char in string:
        char = char.upper()
        if char in morse_code:
            empty_string += f"{morse_code[char]} "
    print(empty_string)

def morse_to_text(string):
    empty_string = ""
    split = string.split()
    for i in split:
        for key,value in morse_code.items():
            if value == i:
                empty_string += key
    print(empty_string)

morse_to_text(".- -.- .... .. .-..")