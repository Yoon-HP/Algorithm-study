#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int N,temp,ans=0,k=1;
    vector<int> v;
    cin >> N;
    temp = N;
    while (temp){
        int a = temp % 10;
        v.push_back(a);
        temp /= 10;
    }
    sort(v.begin(), v.end());
    for (auto i:v){
        ans += i * k;
        k *= 10;
    }
    cout << ans;
    return 0;
}