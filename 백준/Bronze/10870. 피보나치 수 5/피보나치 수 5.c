#include <stdio.h>
int fibo(int n){
    if (n==0){
        return 0;
    }
    else if (n<=2){
        return 1;
    }
    else{
        return fibo(n-2)+fibo(n - 1);
    }
}

int main(){
    int result = 0,n;
    scanf("%d", &n);
    result = fibo(n);
    printf("%d", result);
    return 0;
}