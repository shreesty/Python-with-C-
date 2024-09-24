// factorial.c

#include <stdio.h>

// Recursive function to calculate factorial
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int num = 10;
    printf("Factorial of %d is %d\n", num, factorial(num));
    return 0;
}
