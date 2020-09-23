# morse code dictionary

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',              #dictionary of all character
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': ' '}

def MorseCodeConversion():
    input = str(input("Nhap vao day:  ").upper())                   #input
    result = ''
    for letter in input:
        result += MORSE_CODE_DICT[letter] + ' '                     #look up in the dictionary and add the correct morse code of
                                                                    # each letter to the result string
                                                                    # if it is a space between 2 letter, a " " will be added into result

    print(result)                                                   #print the result
