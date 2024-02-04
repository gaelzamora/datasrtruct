public class testLinkedList {
    public static void main(String[] args) {
        SingleLinkedList list = new SingleLinkedList();
        
        list.viewNodos();
        list.appendToTail(8);
        list.appendToTail(9);
        list.appendToTail(4);
        list.appendToTail(2);
        list.deleteNode(4);
        list.viewNodos();
    }
    
}
