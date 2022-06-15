/**
 * Creates a Generator object which stores plain text, the encryption operations performed on plaintext, 
 * a value for where the generated password will be used, and the generated password
 * @author Kurt Ger
 */

import java.util.*;


public class Generator {
    
    private String origText;    //before
    private ArrayList<String> methods;   //place to store what ops have been performed on original text
    private String lock;    //site/platform the password will go
    private String psw;     //after

    Generator(){
        origText = null;
        methods = null;
        lock = null;
        psw = null;
    }

    public void setOrig(String orig){
        origText = orig;
    }
    public String getOrig(){
        return origText;
    }

    public void addOp(String op){
        methods.add(op);
    }
    public ArrayList<String> getOps(){
        return methods;
    }

    public void setLock(String site){
        lock = site;
    }
    public String getLock(){
        return lock;
    }

    public void setPass(String pass){
        psw = pass;
    }
    public String getPass(){
        return psw;
    }


}
