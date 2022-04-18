# include <stdio.h>
int main(){
    int a, b, c, result[10]={0},temp;
    scanf("%d %d %d", &a, &b, &c);
    temp = a * b * c;
    while (temp){
        result[temp % 10]++;
        temp /= 10;
    }
    for (int i = 0; i < 10;i++){
        printf("%d\n", result[i]);
    }
    return 0;
}