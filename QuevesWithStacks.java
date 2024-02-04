import java.util.ArrayDeque;
import java.util.Deque;

public class QuevesWithStacks{
    Deque<Integer> firstStack = new ArrayDeque<>();    
    Deque<Integer> secondStack = new ArrayDeque<>();

    public static void main(String[] args) {
        QuevesWithStacks queueWithStacks = new QuevesWithStacks();

        System.out.println(queueWithStacks.isEmpty());
        queueWithStacks.add(1);        
        queueWithStacks.add(2);
        queueWithStacks.add(3);
        queueWithStacks.remove();
        System.out.println(queueWithStacks.size());
        queueWithStacks.add(4);
        System.out.println(queueWithStacks.isEmpty());
        System.out.println(queueWithStacks.size());

    }

    public void add(Integer value) {
        firstStack.push(value);
    }

    public Integer peek() {
        dumpElementsIntoSecondStack();
        return secondStack.peek();
    }

    public Integer remove() {
        dumpElementsIntoSecondStack();
        return secondStack.pop();
    }

    private void dumpElementsIntoSecondStack() {
        if(secondStack.isEmpty()) {
            while (!firstStack.isEmpty()) {
                secondStack.push(firstStack.pop());
            }
        }
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public int size() {
        return firstStack.size() + secondStack.size();
    }
}