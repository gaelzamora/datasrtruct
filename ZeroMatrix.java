public class ZeroMatrix {
    public static void main(String[] args) {
        int[][] matrix = {{2,0,4},{9,2,3},{0,8,0}};

        zeroMatrix(matrix);
    }

    public static void zeroMatrix(int[][] matrix) {
        boolean firstRowHasZero = hasFirstRowAnyZero(matrix);        
        boolean firstColHasZero = hasFirstColAnyZero(matrix);

        checkForZeroes(matrix);

        processRow(matrix);
        processColumns(matrix);

        if(firstRowHasZero){
            setRowToZero(matrix, 0);
        }
        if(firstColHasZero){
            setColToZero(matrix, 0);
        }
    }

    private static boolean hasFirstRowAnyZero(int[][] matrix) {
        for(int i = 0; i < matrix[0].length; i++) {
            if(matrix[0][i] == 0) return true;
        }
        return false;
    }

    private static boolean hasFirstColAnyZero(int[][] matrix) {
        for(int i = 0; i < matrix.length; i++) {
            if(matrix[i][0] == 0) return true;
        }
        return false;
    }

    private static void checkForZeroes(int[][] matrix) {
        for(int row = 1; row<matrix.length; row++) {
            for(int col = 1; col < matrix[0].length; col++) {
                if(matrix[row][col] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        }
    }

    private static void processRow(int[][] matrix) {
        for(int row = 0; row<matrix.length; row++) {
            if(matrix[row][0] == 0) {
                setRowToZero(matrix, row);
            }
        }
    }

    private static void setRowToZero(int[][] matrix, int row) {
        for(int col = 0; col<matrix[0].length; col++ ) {
            matrix[row][col] = 0;
        }
    }

    private static void processColumns(int[][] matrix) {
        for(int col = 0; col < matrix[0].length; col++) {
            if(matrix[0][col] == 0) {
                setColToZero(matrix, col);
            }
        }
    }

    private static void setColToZero(int[][] matrix, int col) {
        for(int row = 0; row<matrix[0].length; row++ ) {
            matrix[row][col] = 0;
        }
    }
}
