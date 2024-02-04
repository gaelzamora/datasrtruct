import java.util.ArrayDeque;
import java.util.Deque;


public class ValidParenthesis {
    public static void main(String[] args) {
        System.out.println(isValid("([]){"));
    }

    public static boolean isValid(String s) {
        // ([]){
        Deque<Character> stack = new ArrayDeque<>();
        
        // (
        for(char c : s.toCharArray()) {
            if(c == '(' || c == '{' || c == '[') {
                // ) ] 
                stack.push(getOpposite(c));
            } else {
                
                if(stack.isEmpty() || stack.pop() != c) return false;
            }
        }
        return stack.isEmpty();
    }

    public static Character getOpposite(char c) {
        if(c == '(') return ')';        
        if(c == '{') return '}';
        if(c == '[') return ']';

        return '0';
    }
}