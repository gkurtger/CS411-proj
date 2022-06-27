import java.util.*;
public class Vigenere {
    boolean state;      //same as caesar: true for encrypt, false for decrypt
    String key;
    
    private Vigenere(boolean stateInp, String keyInp){
        state = stateInp;
        key = keyInp;
    }
    
    private static String vigEnc(Generator genned, Vigenere op){
        String plain = null;
        String result = "";
        String key = op.key;

        int txtTrack = 0;
        int keyTrack = 0;

        if(genned.getPass() == null){
            plain = genned.getOrig();
        }
        else{
            plain = genned.getPass();
        }

        while(txtTrack<plain.length()){
            char txtChar = plain.charAt(txtTrack);
            char keyChar = key.charAt(keyTrack%key.length());
            if(Character.isAlphabetic(txtChar)){
                if(Character.isUpperCase(txtChar) && Character.isUpperCase(keyChar)){
                    int insVal = (int)txtChar + (int)keyChar - 65;
                    if(insVal>90){
                        insVal -= 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
                else if(Character.isUpperCase(txtChar) && Character.isLowerCase(keyChar)){
                    char truKeyChar = Character.toUpperCase(keyChar);
                    int insVal = (int)txtChar + (int)truKeyChar - 65;
                    if(insVal>90){
                        insVal -= 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
                else if(Character.isLowerCase(txtChar) && Character.isLowerCase(keyChar)){
                    int insVal = (int)txtChar + (int)keyChar - 97;
                    if(insVal>122){
                        insVal -= 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
                else if(Character.isLowerCase(txtChar) && Character.isUpperCase(keyChar)){
                    char truKeyChar = Character.toLowerCase(keyChar);
                    int insVal = (int)txtChar + (int)truKeyChar - 97;
                    if(insVal>122){
                        insVal -= 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
            }
            else{
                result += txtChar;
                txtTrack++;
            }
        }
        
        return result;
    }

    private static String vigDec(Generator genned, Vigenere op){
        String plain = null;
        String result = "";
        String key = op.key; 

        int txtTrack = 0;
        int keyTrack = 0;

        if(genned.getPass() == null){
            plain = genned.getOrig();
        }
        else{
            plain = genned.getPass();
        }

        while(txtTrack<plain.length()){
            char txtChar = plain.charAt(txtTrack);
            char keyChar = key.charAt(keyTrack%key.length());
            if(Character.isAlphabetic(txtChar)){
                if(Character.isUpperCase(txtChar) && Character.isUpperCase(keyChar)){
                    int insVal = (int)txtChar - (int)keyChar + 65;
                    if(insVal<65){
                        insVal += 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
                else if(Character.isUpperCase(txtChar) && Character.isLowerCase(keyChar)){
                    char truKeyChar = Character.toUpperCase(keyChar);
                    int insVal = (int)txtChar - (int)truKeyChar + 65;
                    if(insVal<65){
                        insVal += 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
                else if(Character.isLowerCase(txtChar) && Character.isLowerCase(keyChar)){
                    int insVal = (int)txtChar - (int)keyChar + 97;
                    if(insVal<97){
                        insVal += 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
                else if(Character.isLowerCase(txtChar) && Character.isUpperCase(keyChar)){
                    char truKeyChar = Character.toLowerCase(keyChar);
                    int insVal = (int)txtChar - (int)truKeyChar + 97;
                    if(insVal<97){
                        insVal += 26;
                    }
                    result += (char)insVal;
                    txtTrack++;
                    keyTrack++;
                }
            }
            else{
                result += txtChar;
                txtTrack++;
            }
        }
        
        return result;
    }
    
    
    
    public static String vigExe(Generator genned){
        Scanner lidar = new Scanner(System.in);
        System.out.println("Enter eNcrypt/Decrypt: ");
        String statePing = lidar.nextLine();

        boolean statePut = false;
        String keyPut = null;

        String result = null;

        if(statePing.toUpperCase().equals("N")){   //these are problems that will be solved by the gui. you will select encrypt/decrypt from there to make this work.
            statePut = true;
            System.out.println("Enter key (must only consist of letters): ");
            keyPut = lidar.nextLine();
            boolean validKey = keyPut.matches("[a-zA-Z]+");
            while(!validKey){
                System.out.println("Enter key (must only consist of letters): ");
                keyPut = lidar.nextLine();
                validKey = keyPut.matches("[a-zA-Z]+");
            }
        }
        else if(statePing.toUpperCase().equals("D")){
            System.out.println("Enter key (must only consist of letters): ");
            keyPut = lidar.nextLine();
            boolean validKey = keyPut.matches("[a-zA-Z]+");
            while(!validKey){
                System.out.println("Enter key (must only consist of letters): ");
                keyPut = lidar.nextLine();
                validKey = keyPut.matches("[a-zA-Z]+");
            }
        }

        Vigenere cipherator = new Vigenere(statePut, keyPut);
        if(cipherator.state){
            result = vigEnc(genned, cipherator);
        }
        else{
            result = vigDec(genned, cipherator);
        }
        
        lidar.close();
        return result;
    }
}

//must check for valid keys; keys must be letters only (entered key is case-insensitive)
