#include<stdio.h>

int main() {
    int sumOfSquares = 0;
    int squareOfSum = 0;
    
    int i;
    for(i=1; i<=100; i++) {
        sumOfSquares += i*i;
    }
    for(i=1; i<=100; i++) {
        squareOfSum += i;
    }
    squareOfSum *= squareOfSum;
    
    printf("The answer is: %d", squareOfSum-sumOfSquares);
    
    return 0;
}
