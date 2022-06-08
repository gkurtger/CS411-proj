public class Atbash {
    
    public static String atbExe(Generator genned){
        String plain = genned.getOrig();
        String cipher = "";         //there is a matrix joke we can make here just like prof ibrahim did

        for(int i=0; i<plain.length(); i++){
            char worked = plain.charAt(i);
            if (Character.isAlphabetic(worked)){
                int workedVal = (int) worked;
                if ( (workedVal>=65) && (workedVal<=90) ){
                    int addedVal = 155-workedVal;
                    char added = (char)addedVal;
                    cipher = cipher+added;
                }
                else if ( (workedVal>=97) && (workedVal<=122) ){
                    int addedVal = 219-workedVal;
                    char added = (char)addedVal;
                    cipher = cipher+added;
                }
            }
            else{
                cipher = cipher+worked;
            }
        }
        return cipher;
    }
}



/*
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
 */