public class Caesar{

}



/*
def caesDec():
    shift = input("Enter shift (must be an integer): ")
    while(not shift.isdigit()):
        shift = input("Enter shift (MUST be an integer, I mean it): ")

    shift = int(shift)
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
 */