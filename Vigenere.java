public class Vigenere {
    
}




/*
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
    vigDec()

 */