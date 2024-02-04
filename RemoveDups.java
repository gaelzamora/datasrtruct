import java.util.HashSet;

public class RemoveDups {
    public void removeDups(Node head) {
        if(head == null) return;
        HashSet<Integer> foundValues = new HashSet<>();
        Node current = head;
        foundValues.add(current.value);

        while (current != null && current.next != null){
            if(!foundValues.add(current.next.value)){
                current.next = current.next.next;
            }
            current = current.next;
        }
    }
}
