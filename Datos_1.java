import java.util.HashSet;
import java.util.Set;

/*
 * 
 * Dado un metodo que recibe un String, comprobar si todos los caracteres son unicos o no
 * 
 * isUnique("abcde") --> True
 * isUnique("abcded") --> False
 * 
 * a: b c d e
 * b: c d e
 * 
 * O(n´2)
 * 
 * Tabla Hash
 * a b c d e
 * 
 * for O(N)
 * Consulta el tabla O(1)
 * 
 * O(1)
 */

public class Datos_1 {

    public static void main(String[] args) {
        System.out.println(isUnique("abcded"));    
    }

    private static int NUMBER_OF_CHARS = 128;

    public static boolean isUnique(String s){
        if(s.length() > NUMBER_OF_CHARS) return false;
        Set<Character> characters = new HashSet<>();
        
        for(Character c : s.toCharArray()){
            if(characters.contains(c)) return false;
            characters.add(c);
        }
        return true;
    }

}

