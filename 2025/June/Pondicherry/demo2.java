// import java.util.*;
// public class demo2{

//     public static int prodFn(int n){
//         int fact = 1;
        
//         for(int i = 0; i < n; i++) {
//             fact *= i;
//         }

//         return fact;
//     }

//     public static void main(String args[]) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter n = ");
//         System.out.print("Enter r = ");

//         int n = sc.nextInt();
//         int r = sc.nextInt();

//         sc.close();
//         int numerator = prodFn(n);
//         int denominator = prodFn(n - r) * prodFn(r);
        

//         int perm = numerator/denominator;
//         System.out.println(perm);
//     }
// }

public class demo2 {

    public static int recursionFn(int n) {
        if(n == 0)
            return 0;
        
        return n + recursionFn(n - 1);
    }
    public static void main(String[] args) {
        int n = 5;
        int ans = recursionFn(n);
        System.out.println(ans);
    }
}













