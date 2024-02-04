import java.util.ArrayDeque;
import java.util.Deque;

public class SortStack{
    public static void main(String[] args) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        stack.push(5);
        stack.push(2);
        stack.push(4);

        System.out.println(stack);
        System.out.println(stack.peek());
        
        System.out.println(sort(stack));

    }

    // 1 5 2 4
    // 5 4 2 1
    public static Deque<Integer> sort(Deque<Integer> stack) {
        // []
        // [5, 4, 2, 1]
        Deque<Integer> sortedStack = new ArrayDeque<>();

        // true
        while(!stack.isEmpty()) {
             
            // 1
            Integer element = stack.pop();
            
            // 1 > 2
            while(!sortedStack.isEmpty() && element > sortedStack.peek()) {
             
                stack.push(sortedStack.pop());
            }
            
            sortedStack.push(element);
        }
        return sortedStack;
        /*
        4
        5 
        2
        1

        1
        2
        4
        5
         */
    }
}