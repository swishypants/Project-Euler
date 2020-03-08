#include<stdio.h>

int main() {
    int long num = 600851475143;
    int factor = 2;
    
    while(num>1) {
        if(num%factor==0) {
            num /= factor;
        }
        else {
            factor++;
        }
    }
    printf("The answer is: %d", factor);
    
    return 0;
}
