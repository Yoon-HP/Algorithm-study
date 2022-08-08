#include<iostream>
#include<unordered_set>

using namespace std;

int main(){
    int T, N, M;
    scanf("%d", &T);
    for (int i = 0; i < T;i++){
        unordered_set<int> us;
        scanf("%d", &N);

        for (int j = 0; j < N;j++){
            int temp;
            scanf("%d", &temp);
            us.insert(temp);
        }
        scanf("%d", &M);
        unordered_set<int>::const_iterator got;
        for (int j = 0; j < M;j++){
            int temp;
            scanf("%d", &temp);
            got = us.find(temp);
            if (got==us.end()){
                printf("0\n");
            }else{
                printf("1\n");
            }
        }
    }
    return 0;
}