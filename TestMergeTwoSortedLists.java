public class TestMergeTwoSortedLists {
    public static void main(String[] args) {
        MergeTwoSortedLists merge = new MergeTwoSortedLists();
        Node list1 = new Node(1);
        list1.next = new Node(2);
        list1.next.next = new Node(4);
        list1.next.next.next = new Node(6);

        Node list2 = new Node(2);
        list2.next = new Node(3);
        list2.next.next = new Node(5);

        Node result = merge.mergeTwoLists(list1, list2);
        System.out.println(viewNodes(result));
    }

    private static String viewNodes(Node result) {
        Node current_aux = result;
        String print = ""; 

        while(current_aux != null){
            print+=","+current_aux.value;
            current_aux = current_aux.next;
        }

        return print;
    }
}
