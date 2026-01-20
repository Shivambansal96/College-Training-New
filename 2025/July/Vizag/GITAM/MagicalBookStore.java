import java.util.*;

public class MagicalBookStore {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);


        // // // ODD _ EVEN using BITWISE OPERATOR
        // int n = sc.nextInt();

        // if((n & 1) == 0) {
        //     System.out.println("EVEN");
        // }
        // else {
        //     System.out.println("Odd");
        // }

        // // // GET BIT
        // int n = sc.nextInt();
        // int position = sc.nextInt();

        // int bitMask = 1 << position;
        // String BinaryCodeOfN = Integer.toBinaryString(n);

        // System.out.println(BinaryCodeOfN);

        // if((n & bitMask) == 0) {
        //     System.out.println("Bit was Zero");
        // }
        // else {
        //     System.out.println("Bit was Non-Zero");
        // }

        // // // SET BIT 
        // int n = sc.nextInt();
        // int position = sc.nextInt();

        // int bitMask = 1 << position;
        // // String BinaryCodeOfN = Integer.toBinaryString(n);

        // // System.out.println(BinaryCodeOfN);

        // int num = bitMask | n;

        // System.out.println(num);

        // // // CLEAR BIT 

        // int n = sc.nextInt();
        // int position = sc.nextInt();

        // int bitMask = 1 << position;
        // int newNum = ~(bitMask);
        // int num = n & newNum;

        // System.out.println(num);

        // // // UPDATE BIT

        int oper = sc.nextInt();
        int n = sc.nextInt();
        int position = sc.nextInt();
        int bitMask = 1 << position;

        if(oper ==1) {
            int num = n & bitMask;

            System.out.println(num);
        }
        else {
            int newNum = ~(bitMask);
            int num = n & newNum;
            
            System.out.println(num);
        }


        // System.out.println("Enter the total number of books = ");
        // int n = sc.nextInt();

        // System.out.println("Enter the number of books that can be taken for free per purchase = ");
        // int k = sc.nextInt();

        // int[] arr = new int[n];
        // for(int i = 0; i < n; i++) {
        //     arr[i] = sc.nextInt();
        // }

        // Arrays.sort(arr);

        // int minCost = 0;
        // int left = 0, right = n - 1;
        // while(left <= right) {
        //     minCost += arr[left];
        //     left++;
        //     right -= k;
        // }



    }
}
