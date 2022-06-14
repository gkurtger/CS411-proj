public class Atbash {
    
    public static String atbExe(Generator genned){
        String plain = null;
        if(genned.getPass() == null){
            plain = genned.getOrig();
        }
        else{
            plain = genned.getPass();
        }
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