public class power{
    public static void main(String[] args) {
        System.out.println(powerFunction(4,4));
    }

    public static int powerFunction(int num, int n){
        if(n == 0) return 0;
        int result = 1;

        for(int i=0; i<n; i++){
            result *= num;
        }
        return result;
    }
}