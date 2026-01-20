// #include <stdio.h>

// int main() {
//     int i, j;

//     // Outer loop for each row
//     for (i = 1; i <= 5; i++) {
        
//         // Print leading spaces
//         for (j = 1; j <= 5 - i; j++) {
//             printf(" ");
//         }

//         // Print stars with spaces in between for each row
//         for (j = 1; j <= i; j++) {
//             printf("%d ", j);
//         }

//         // Move to the next line after each row
//         printf("\n");
//     }

//     return 0;
// }

#include <stdio.h>

int main() {
    int i, j, n = 5;  // n is the number of rows in the upper half of the diamond
    // Print upper half of the diamond
    for (i = 1; i <= n; i++) {
        // Print leading spaces
        for (j = 1; j <= n - i; j++) {
            printf(" ");
        }
        // Print numbers
        for (j = 1; j <= i; j++) {
            printf("* ");
        }
        // Move to the next line after each row
        printf("\n");
    }

    // Print lower half of the diamond
    for (i = n - 1; i >= 1; i--) {
        // Print leading spaces
        for (j = 1; j <= n - i; j++) {
            printf(" ");
        }
        // Print numbers
        for (j = 1; j <= i; j++) {
            printf("* ");
        }
        // Move to the next line after each row
        printf("\n");
    }

    return 0;
}
