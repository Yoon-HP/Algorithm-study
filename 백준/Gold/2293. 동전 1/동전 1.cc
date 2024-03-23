#include<iostream>
#include<string.h>
using namespace std;

int dp[10001];
int main(){
    int n, k;
    int value;
    cin >> n >> k;
    memset(dp, 0, (k + 1) * sizeof(int));
    dp[0] = 1;
    for (int i = 0; i < n;i++){
        cin >> value;
        for (int j = value; j <= k;j++){
            dp[j] += dp[j - value];
        }
    }
    cout << dp[k] << endl;
    return 0;
}