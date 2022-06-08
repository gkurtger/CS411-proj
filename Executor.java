
import java.util.*;
public class Executor {     //venari pallin
    



    public static void main(String[] args){
        Generator genned = new Generator();
        
        Scanner lidar = new Scanner(System.in);

        System.out.println("Welcome to the It's-a-Simple-Spell-but-Quite-Unbreakable-inator!");
        System.out.println("Enter original password text: ");
        String origPing = lidar.nextLine();
        genned.setOrig(origPing);
        genned.setPass(Atbash.atbExe(genned));
        System.out.println(genned.getPass());


        lidar.close();

    }

}
