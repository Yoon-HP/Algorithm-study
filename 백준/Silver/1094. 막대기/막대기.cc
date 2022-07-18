#include<iostream>

using namespace std;
int main(){
    int X;
    int start = 64;
    int cnt = 0;
    cin >> X;
    while (X>0){
        if (X%2==1){
            cnt++;
        }
        X /= 2;
    }
    cout << cnt;
    return 0;
}