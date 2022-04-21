#include <stdio.h>
int main(){
    int N, K, i, j;
    scanf("%d %d", &N,&K);
    int arr[N];
    for (i = 0; i < N;i++){
        scanf("%d", &arr[i]);
    }
    int max=0;

    for (i = 0; i < K;i++){
        max += arr[i];
    }
    int temp = max;
    for (i = 1; i <= N - K;i++){
        j = i + K-1;
        temp = temp - arr[i - 1] + arr[j];
        if (max<temp){
            max = temp;
        }
    }
    printf("%d", max);
    return 0;
}