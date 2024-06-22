mourse_En={
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
mourse_Ar={

    'ا': '.-', 'ب': '-...', 'ت': '-', 'ث': '--.', 'ج': '.---', 'ح': '....', 'خ': '---', 'د': '-..', 'ذ': '----',
    'ر': '.-.', 'ز': '--..', 'س': '...', 'ش': '----', 'ص': '--.-', 'ض': '.--', 'ط': '-.-', 'ظ': '..--', 'ع': '..-',
    'غ': '--..', 'ف': '..-.', 'ق': '---.', 'ك': '-.-', 'ل': '.-..', 'م': '--', 'ن': '-.', 'ه': '....', 'و': '.--',
    'ي': '-.--'
}
mourse_Sy={
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def show_mourseAR(user_message):
    for m in user_message:
        if m == '':
            print("|",end='')
        print(mourse_Ar[m] , end='' )
    print('\n')
        
def show_mourseEN(user_message):
    for m in user_message:
        if m == '':
            print("|",end='')
        print(mourse_En[m],end='')
    print('\n')
        
def show_mourseSY(user_message):
    for m in user_message:
        if m == '':
            print("|",end='')
        print(mourse_Sy[m],end='')
    print('\n')
print("=======================\nWelcom in mourse code\n=======================")
print("When you want to quite the game enter: 'quitgame'\n")

while True:
     user_message=input('Enter YOUR MESSAGE : ').upper()
     if user_message == "QUITGAME":
       exit('FINISH')
     m1,m2=0,0
     for ch in user_message:
       
        if ch in mourse_Ar:
            m1=1
        elif ch in mourse_En:
            m2=1
        else:
            print('Your message include Unsportted letter of mourse code...')
     if 1==m1 and 1==m2:
        print('Your message has a mixed langhage...')
     elif 1==m1 and 1 != m2:
        show_mourseAR(user_message)
     elif 1==m2 and 1!=m1:
        show_mourseEN(user_message)