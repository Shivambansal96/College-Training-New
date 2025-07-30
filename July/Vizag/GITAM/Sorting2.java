// class Sorting {
//     public static void main(String[] args) {
//         int[] arr = {30, 32, 13, 41, 4, 44, 13};
//         for (int i = 1; i < arr.length; i++) {
//             for (int j = i - 1; j >= 0; j--) {
//                 if (arr[j] > arr[j + 1]) {
//                     int temp = arr[j];
//                     arr[j] = arr[j + 1];
//                     arr[j + 1] = temp;
//                 } else {
//                     break;
//                 }
//             }
//         }

//         for (int num: arr) {
//             System.out.print(num + " ");
//         }
//     }
// }



class Sorting2 {
    public static void main(String[] args) {
        int[] arr = {30, 32, 13, 41, 4, 44, 13};
        
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
        
        for (int num: arr) {
            System.out.print(num + " ");
        }
    }
}