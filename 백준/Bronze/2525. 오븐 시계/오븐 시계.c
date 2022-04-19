#include <stdio.h>
int main(){
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    if ((B+C)/60>=1){
        int temp = (B + C) / 60;
        if ((temp+A)>=24){
            printf("%d ", (temp + A) - 24);
        }
        else{
            printf("%d ", (temp + A));
        }
    }
    else{
        printf("%d ", A);
    }
    printf("%d", (B + C) % 60);
    return 0;
}