MrCd_Dict= { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
             'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
             'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
             'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
             'X':'-..-', 'Y':'-.--', 'Z':'--..',
             '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
             '7':'--...', '8':'---..', '9':'----.', '0':'-----',
             ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
             '(':'-.--.', ')':'-.--.-'}

print("Enter 1 to encode a text(Eng) into Morse")
print("Enter 2 to decode a Morse Code")
c=(input("Enter your Choice: "))

if c=='1':
    m=input("Enter the text(Eng): ")
    m=m.upper()
    r=''

    for l in m:
        if l!=' ':
            r+=MrCd_Dict[l]+' '
        else:
            r+=' '
            
    print("Morse code equivalent:", end='')
    print(r)

elif c=='2':
    m=input("Enter the Morse Code: ")
    m+=' '
    r= ''
    ct= ''

    for l in m:
        if (l!=' '):
            i=0
            ct+=l
        else:
            i+=1
            if i==2 :
                r+=' '
            else:
                r+=list(MrCd_Dict.keys())[list(MrCd_Dict.values()).index(ct)]
                ct=''
 
    print("English Translation:")
    
    r=r.title()
    print(r)
