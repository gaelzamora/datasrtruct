public class InvertBinaryTree {
    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(3);
        root.right = new Node(4);
        root.left.left = new Node(5);
        root.left.right = new Node(9);
        root.right.left = new Node(6);

        System.out.println(invertTree(root));
    }

    public static Node invertTree(Node root) {
        if(root == null) return null;

        Node tmp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(tmp);
        if(root.left != null && root.right != null) {
            System.out.println(root.left.value);
            System.out.println(root.right.value);
        }
        
        return root;
    }
}
