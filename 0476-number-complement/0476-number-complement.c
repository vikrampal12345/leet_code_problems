#include <stdio.h>
#include <math.h>

int findComplement(int num) {
    int arr[32];
    int new_arr[32];
    int size = 0;
    int i;

    // Decimal to Binary
    while (num > 0) {
        arr[size++] = num % 2;
        num /= 2;
    }

    // Reverse binary array
    for (i = 0; i < size / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - i - 1];
        arr[size - i - 1] = temp;
    }

    // Find complement
    for (i = 0; i < size; i++) {
        if (arr[i] == 0) {
            new_arr[i] = 1;
        } else {
            new_arr[i] = 0;
        }
    }

    // Reverse complement array
    for (i = 0; i < size / 2; i++) {
        int temp = new_arr[i];
        new_arr[i] = new_arr[size - i - 1];
        new_arr[size - i - 1] = temp;
    }

    // Binary to Decimal
    int sum = 0;
    for (i = 0; i < size; i++) {
        sum += new_arr[i] * (int)pow(2, i);
    }

    return sum;
}

