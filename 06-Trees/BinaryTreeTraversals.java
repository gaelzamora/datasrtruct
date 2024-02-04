public class BinaryTreeTraversals {
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);

        root.left.left = new Node(4);
        root.left.right = new Node(5);

        root.right.right = new Node(6);

        root.left.left.left = new Node(7);

        root.left.right.left = new Node(8);

        System.out.println("IN ORDER TRAVERSAL: ");
        inOrderTraversal(root);

        System.out.println("PRE ORDER TRAVERSAL: ");
        preOrderTraversal(root);

        System.out.println("POST ORDER TRAVERSAL: ");
        postOrderTraversal(root);
    }

    public static void inOrderTraversal(Node node) {
        // true 
        if(node != null) {
            // 2 
            inOrderTraversal(node.left);
            System.out.println(node.value + " ");
            inOrderTraversal(node.right);
        }
    }   

    public static void preOrderTraversal(Node node) {
        if(node != null) {
            System.out.println(node.value + " ");
            preOrderTraversal(node.left);
            preOrderTraversal(node.right);
        }
    }

    public static void postOrderTraversal(Node node) {
        if(node != null) {
            postOrderTraversal(node.left);
            postOrderTraversal(node.right);
            System.out.println(node.value + " ");
        }
    } 
}