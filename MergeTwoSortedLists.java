public class MergeTwoSortedLists{
    public Node mergeTwoLists(Node list1, Node list2){
        Node aux = new Node(-1);
        Node current = aux;
        // 4 -> 5 -> 8 | 3 -> 5 -> 6 -> 9

        while(list1 != null && list2 != null){//false
            if(list1.value <= list2.value){// 8 <= 9 true
                current.next = list1; // -1 -> 3 -> 4 -> 5 -> 5 -> 6 -> 8
                list1 = list1.next; // null
            } else {
                current.next = list2; // -1 -> 3 -> 4 -> 5 -> 5 -> 6 
                list2 = list2.next; // 9 
            }
            current = current.next; // 8
        }

        if(list1 != null){
            current.next = list2;
        } else {
            current.next = list1;
        }
        // -1 -> 3 -> 4 -> 5 -> 5 -> 6 -> 8 -> 9
        
        return aux.next;
        // 3 -> 4 -> 5 -> 5 -> 6 -> 8 -> 9
    }
    public static void viewNodes(Node list){
        Node current_aux = list;
        String print = ""; 

        while(current_aux != null){
            print+=","+current_aux.value;
            current_aux = current_aux.next;
        }

        System.out.println(print);
    }
}