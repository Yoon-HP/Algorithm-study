#include <unordered_map>
#include <iostream>

using namespace std;

int main(){
    ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
    int T;
    cin >> T;
    for (int test = 1; test <= T;test++){
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
            char temp[51];
            cin >> temp;
            if (um.find(temp)!=um.end()){
                ans++;
            }
        }
        printf("#%d %d\n", test, ans);
    }
    return 0;
}