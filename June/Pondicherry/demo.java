import java.util.Scanner;

public class demo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // int rows = sc.nextInt();
        // int cols = sc.nextInt();

        System.out.print("Enter the number of rows = ");
        int rows = sc.nextInt();

        System.out.print("Enter the number of rows = ");
        int cols = sc.nextInt();
        int[][] marks = new int[rows][cols];

        // INPUT
        System.out.print("Enter the elements in the matrix = ");
         for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                marks[i][j] = sc.nextInt();
                // System.out.print(i + "" + j + " ");
            }
        }

        System.out.print("Enter the target = ");
        int target = sc.nextInt();

        // OUTPUT 
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                if(marks[i][j] == target){
                    System.out.print(i + "" +  j + " ");
                    return;
                }
            }
        }

         // System.out.print("Enter the size of the array = ");
        // // int size = sc.nextInt();
        // // int[] arr = new int[size];

        // int[] arr = {46, 312, 1500, 42, 10};
        // System.out.print("Enter the elements of the array = ");
        // // for(int i = 0; i < arr.length; i++) 
        // //     arr[i] = sc.nextInt();

        // int min = arr[0];
        // int max = arr[0];

        // int sum = 0;

        // for(int i = 0; i < arr.length; i++) {
        //     sum = sum + arr[i];
        //     // if(arr[i] > max) max = arr[i];
        //     // if(arr[i] < min) min = arr[i];

            
        // }
        
        // int avg = sum/arr.length;
        // System.out.println("Maximum Value = " + max);
        // System.out.println("Minimum Value = " + min);
        // System.out.println("Sum = " + sum);
        // System.out.println("Average Value = " + avg);

        
        // // System.out.print("Enter the size of the array = ");
        // // int size = sc.nextInt();

        // int[] marks = new int[size];

        // // INPUT
        // System.out.print("Enter the numbers in the array = ");
        // for(int i = 0; i < size; i++) {
        //     marks[i] = sc.nextInt();
        // }

        // System.out.print("Enter the target = ");
        // int target = sc.nextInt();

        // for(int i = 0; i < size; i++) {
        //     if(marks[i] == target){
        //         System.out.print(i + " ");
        //         break;
        //     }
        // }


















        // // 1D Array
        // int[] marks = new int[3];

        // System.out.println("Enter marks of P = ");
        // marks[0] = sc.nextInt();

        // System.out.println("Enter marks of C = ");
        // marks[1] = sc.nextInt();

        // System.out.println("Enter marks of B = ");
        // marks[2] = sc.nextInt();

        // for(int i:marks) {
        //     System.out.println(i);
        // }

        // // 2D Array
        // int[][] nums = new int[3][5];

        // //INPUT
        // for(int i = 0; i < 3; i++) {
        //     for(int j = 0; j < 5; j++) {
        //         nums[i][j] = sc.nextInt();
        //     }
        // }

        // int target = 3;

        // //OUTPUT
        // for(int i = 0; i < 3; i++) {

        //     for(int j = 0; j < 5; j++) {
        //         if(nums[i][j] == target) {
        //             System.out.print(i + "" + j + " ");
        //             break;
        //         }
        //     }
        //     System.out.println();
        // }



        

    }
}




