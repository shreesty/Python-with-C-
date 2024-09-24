#include <stdio.h>
// Function to calculate the square of a number
int square(int n) {
    return n * n;
}

// Function to concatenate two strings
void concat_strings(const char* str1, const char* str2, char* result) {
    sprintf(result, "%s%s", str1, str2);
}

// Function to check if a number is prime
int is_prime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i <= n/2; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}
