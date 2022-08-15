#include <iostream>

int arr[1000001];
int buf[1000001];
long long ans;

void mergeSort(int start,int end){
    if (start<end){
        int mid = start+(end-start)/2;
        mergeSort(start, mid);
        mergeSort(mid+1, end);
        int i = start, j = mid + 1, k = start;
        while(i<=mid && j<=end){
            if (arr[i]<arr[j]){
                buf[k++] = arr[i++];
            }else{
                ans += (mid - i + 1);
                buf[k++] = arr[j++];
            }
        }
        while (i<=mid){
            buf[k++] = arr[i++];
        }
        while (j<=end){
            ans += (mid - i + 1);
            buf[k++] = arr[j++];
        }
        for (int i = start; i <= end;i++){
            arr[i] = buf[i];
        }
    }
}

int main(){
    int N;
    ans = 0;
    scanf("%d", &N);
    for (int i = 0; i < N;i++){
        scanf("%d", &arr[i]);
    }
    mergeSort(0, N - 1);
    printf("%lld",ans);
}