
import java.util.*;
public class Executor {     //venari pallin
    



    public static void main(String[] args){
        Generator genned = new Generator();
        
        Scanner lidar = new Scanner(System.in);

        System.out.println("Welcome to the It's-a-Simple-Spell-but-Quite-Unbreakable-inator!");
        
        System.out.println("Enter location for generated password: ");
        String sitePing = lidar.nextLine();
        genned.setLock(sitePing);
        
        System.out.println("Enter original password text: ");
        String origPing = lidar.nextLine();
        genned.setOrig(origPing);
        
        System.out.println("Choose cipher type [C/A/V]: ");
        String opPing = lidar.nextLine();
        
        if(opPing.toUpperCase().equals("C")){
            Caesar.caesExe(genned);
            System.out.println(genned.getPass());
        }

        else if(opPing.toUpperCase().equals("A")){
            Atbash.atbExe(genned);
            System.out.println(genned.getPass());
        }

        
        else if(opPing.toUpperCase().equals("V")){
            Vigenere.vigExe(genned);
            System.out.println(genned.getPass());
        }

        lidar.close();

    }

}
