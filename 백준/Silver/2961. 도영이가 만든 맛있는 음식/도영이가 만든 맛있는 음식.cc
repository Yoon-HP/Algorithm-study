#include<iostream>
#include<vector>
#include<cstdlib>
using namespace std;
int main(){
    
    int S, B;
    int N;
    int ans = 1000000001;
    vector<pair<int, int>> v;
    scanf("%d", &N);
    for (int i = 0; i < N;i++){
        scanf("%d %d", &S, &B);
        v.push_back({S, B});
    }
    int A = (1<<N)-1;
    for (int subset = A; subset; subset=((subset-1) & A)){
        int temp_S = 1;
        int temp_B = 0;
        for (int j = 0; j < N;j++){
            if (subset&(1<<j)){
                temp_S *= v[j].first;
                temp_B += v[j].second;
                
            }
        }
        if (abs(temp_S-temp_B)<ans){
            ans = abs(temp_S - temp_B);
        }
    }
    printf("%d", ans);
    return 0;
}