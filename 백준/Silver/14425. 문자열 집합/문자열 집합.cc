#include <unordered_map>
#include <iostream>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
	cin.tie(NULL);

    unordered_map<string, string> um;
    int N, M;
    int ans = 0;
    cin >> N >> M;
    for (int i = 0; i < N;i++){
        string temp;
        cin >> temp;
        um.insert({temp, temp});
    }
    for (int i = 0; i < M;i++){
        string temp;
        cin >> temp;
        if (um.find(temp)!=um.end()){
            ans++;
        }
    }
    printf("%d\n",ans);
    return 0;
}