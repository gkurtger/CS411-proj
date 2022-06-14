import java.util.*;
public class Caesar{

    boolean state;  //true for encrypt, false for decrypt
    int shift;


    private Caesar(boolean stateInp, int shiftInp){
        state = stateInp;
        shift = shiftInp;
    }

    public static String caesDec(Generator genned, Caesar op){
        String plain = null;
        if(genned.getPass() == null){
            plain = genned.getOrig();
        }
        else{
            plain = genned.getPass();
        }
        String cipher = "";

        for(int i=0; i<plain.length(); i++){
            char worked = plain.charAt(i);
            int trueShift = op.shift%26;
            if (Character.isAlphabetic(worked)){
                int workedVal = (int) worked;
                int shiftedVal = workedVal - trueShift;
                
                if( (shiftedVal>90)&&(workedVal<97) ){
                    shiftedVal -= 26;
                    char added = (char)shiftedVal;
                    cipher = cipher + added;
                }                
                else if( (shiftedVal<65) || (shiftedVal<97 && workedVal>97) ){
                    shiftedVal += 26;
                    char added = (char)shiftedVal;
                    cipher = cipher + added;
                }
                                
                else{
                    char added = (char)shiftedVal;
                    cipher = cipher + added;
                }
                
            }
            else{
                cipher = cipher+worked;
            }
        }
        return cipher;
    }

    public static String caesEnc(Generator genned, Caesar op){
        String plain = null;
        if(genned.getPass() == null){
            plain = genned.getOrig();
        }
        else{
            plain = genned.getPass();
        }
        String cipher = "";

        for(int i=0; i<plain.length(); i++){
            char worked = plain.charAt(i);
            int trueShift = op.shift%26;
            if (Character.isAlphabetic(worked)){
                int workedVal = (int) worked;
                int shiftedVal = workedVal + trueShift;
                
                if( (shiftedVal>90)&&(workedVal<97) ){
                    shiftedVal -= 26;
                    char added = (char)shiftedVal;
                    cipher = cipher + added;
                }                
                else if( (shiftedVal<65) || (shiftedVal<97 && workedVal>97) ){
                    shiftedVal += 26;
                    char added = (char)shiftedVal;
                    cipher = cipher + added;
                }
                                
                else{
                    char added = (char)shiftedVal;
                    cipher = cipher + added;
                }
                
            }
            else{
                cipher = cipher+worked;
            }
        }
        return cipher;
    }

    public static String caesExe(Generator genned){
        Scanner lidar = new Scanner(System.in);
        System.out.println("Enter eNcrypt/Decrypt: ");
        String origPing = lidar.nextLine();
        if(origPing.equals("N")){   //these are problems that will be solved by the gui. you will select encrypt/decrypt from there to make this work.
            System.out.println("Enter shift: ");
            int shiftPut = lidar.nextInt();
            Caesar cipherator = new Caesar(true, shiftPut);
            lidar.close();
            return caesEnc(genned, cipherator);
        }
        else if(origPing.equals("D")){
            System.out.println("Enter shift: ");
            int shiftPut = lidar.nextInt();
            Caesar cipherator = new Caesar(false, shiftPut);
            lidar.close();
            return caesDec(genned, cipherator);
        }

        lidar.close();
        return null;    //THIS IS DEADLY AT THE MOMENT
    }
}
