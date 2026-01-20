#include <stdio.h>

int main() {

    int arr[] = {10, 20, 30};

    int n = 3, A = 0, B = 0, C = 0;

    for(int i = 0; i < n; i++) {

        if(arr[i] % 3 == 1) 
            A += (arr[i]/3) + 1;
        else if(arr[i] % 3 == 2) 
            A += (arr[i]/3) + 1;
        else
            A += (arr[i]/3);
    }
    printf("A received %d chocolates.", A);







}

