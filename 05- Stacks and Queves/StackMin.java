import java.util.ArrayDeque;
import java.util.Deque;

public class StackMin {

    private static Deque<Integer> valueStack = new ArrayDeque<>();
    private static Deque<Integer> minStack = new ArrayDeque<>();

    public static void main(String[] args) {
        minStack.push(6);
        minStack.push(4);
        minStack.push(8);
        minStack.push(1);

        System.out.println
    }

    // []
    // [6, 4, 8, 1]

    public void push(Integer data) {
        // 
        valueStack.push(data);
        if(minStack.isEmpty() || data < minStack.peek()) {
            minStack.push(data);
        }
    }

    public int pop() {
        int value = minStack.pop();
        if(value == minStack.peek()){
            minStack.pop();
        }
        return value;
    }

    public int min() {
        return minStack.peek();
    }
}