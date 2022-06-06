def caesDec():
    shift = input("Enter shift (must be an integer): ")
    while(not shift.isdigit()):
        shift = input("Enter shift (MUST be an integer, I mean it): ")

    shift = int(shift)
    #shift = ( int(shift) % 26)*-1   #because if you enter 3 you get 3 letters before not after, something with cipher definition and intuitive understanding (this line caused a bug and should not be unshuttered)
    inp = input("Enter text to decrypt: ")
    res = ""

    for ch in inp:
        if ch.isalpha():
            bef = ord(ch)
            aft = bef + shift
            
            if (aft>90 and bef<97) or aft>122:
                aft -= 26
            elif aft<65 or (aft<97 and bef>97):
                aft += 26
            
            res = res + chr(aft)
        
        else:
            res = res + ch

    print("\nDecrypted text: " + res)
    
def caesEnc():
    shift = input("Enter shift (must be an integer): ")
    while(not shift.isdigit()):
        shift = input("Enter shift (MUST be an integer, I mean it): ")

    shift = int(shift)
    #shift = ( int(shift) % 26)*-1   #the same thing does not happen here what the fuck (line shuttered same reason as before)
    inp = input("Enter text to encrypt: ")
    res = ""

    for ch in inp:
        if ch.isalpha():
            bef = ord(ch)
            aft = bef + shift
            
            if (aft>90 and bef<97) or aft>122:
                aft -= 26
            elif aft<65 or (aft<97 and bef>97):
                aft += 26
            
            res = res + chr(aft)
        
        else:
            res = res + ch
    
    print("\nEncrypted text: " + res)

def atbDec():
    inp = input("Enter text to decrypt: ")
    res = ""

    for ch in inp:
        if ch.isalpha():
            bef = ord(ch)
            if bef>=65 and bef<=90:
                aft = 155-bef
            elif bef>=97 and bef<=122:
                aft = 219-bef

            res = res + chr(aft)

        else:
            res = res + ch

    print("\nDecrypted text: " + res)

def atbEnc():
    inp = input("Enter text to encrypt: ")
    res = ""

    for ch in inp:
        if ch.isalpha():
            bef = ord(ch)
            if bef>=65 and bef<=90:
                aft = 155-bef
            elif bef>=97 and bef<=122:
                aft = 219-bef

            res = res + chr(aft)

        else:
            res = res + ch

    print("\nEncrypted text: " + res)

def vigDec():
    key = input("Enter key: ")
    inp = input("Enter text to decrypt: ")
    res = ""

    keyStr = key.upper()

    grid = vigSqGen()
    inp2 = inp.upper()

    keyTrack = 0
    txtTrack = 0

    while txtTrack < len(inp2):
        k = ord(keyStr[keyTrack%len(keyStr)])-65
        if inp2[txtTrack].isalpha():
            j = grid[k].find(inp2[txtTrack])
            res = res + grid[0][j]
            keyTrack += 1
            txtTrack += 1
        else:
            res = res + inp2[txtTrack]
            txtTrack += 1

    print("\nDecrypted text: " + res)

def vigEnc():
    print("Under construction!")
    #print("\nEncrypted text: " + res)
    #print(res)


def runner():
    print("\n\n\n")

    ciph = input("Which cipher shall we be tackling today? [C/A/V]: ")
    while(ciph.upper() not in "CAV"):
        ciph = input("Remember, you need to use the first letters of what you want. See Limitations. [C/A/V]: ")
    
    way = input("Do we want to eNcrypt or Decrypt? [N/D]: ")
    while(way.upper() not in "ND"):
        way = input("You can't really do anything else with ciphers, you know. [N/D]: ")

    if way.upper() == 'N':
        if ciph.upper() == 'C':
            caesEnc()
        elif ciph.upper() == 'A':
            atbEnc()
        elif ciph.upper() == 'V':
            vigEnc()

    elif way.upper() == 'D':
        if ciph.upper() == 'C':
            caesDec()
        elif ciph.upper() == 'A':
            atbDec()
        elif ciph.upper() == 'V':
            vigDec()

def vigSqGen():
    seed = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sq = []
    i = 0
    while i<26:
        sq.append(seed[i:i+26])
        i += 1

    return sq


def main():
    print("This here is a project I am using to combine my knowledge of baseline by-hand encryption methods and programming (not to mention procrastination).")
    print("As you select a method to de/cipher text with, use their first letter as input (see Limitations).")
    print("\nLimitations:")
    print("Only works with English text (because I know the secrets of the virgin ASCII but not those of the chad Unicode).")
    print("Cannot read files. Ctrl-C-V keys quiver in the face of this abomination (not to mention it can only process one line at a time).")
    #print("Can only actually be used for two types of cipher at the moment. Signs of UNDER CONSTRUCTION are placed so I can get off my ass and finish main.")
    print("Because my knowledge of any encryption comes from having watched Gravity Falls (and having read a kids' book about it) as a kid, I can only code Caesar, Atbash, or Vigenère into this.")
    print("Vigenère encryption under construction.")
    #print("If you don't enter a number for a Caesar shift, the program catches fire because I don't remember how to error catch in Python.")
    input("\nEnter anything to continue: ")

    runner()
    keep = True
    while keep:
        ans = input("Will you be doing any more freshwater spy work? [y/n]:")
        while(ans.upper() not in "YN"):
            ans = input("y/n here means 'yes/no' and not 'your name'. [y/n]:")
        
        if ans.upper() == 'Y':
            runner()
        elif ans.upper() == 'N':
            keep = False
            print("\nThank you for using this program for your extremely niche surreptitious business!")

main()

#V rapelcgrq guvf zrffntr fb Cnesnvg jba'g or noyr gb ernq vg yby jub'f gur ivetva abj