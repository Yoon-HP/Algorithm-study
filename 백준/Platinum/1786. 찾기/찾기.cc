#include<iostream>
#include<string>

using namespace std;

int lps[1000001]={0};
int ans;
int ans_index[1000001] = {0};

void computeLPS(string pat);
void KMPSearch(string pat, string txt);

int main(){
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string pat, txt;
    getline(cin, txt);
    getline(cin, pat);
    KMPSearch(pat, txt);
    cout << ans << endl;
    for (int i = 0; i < ans;i++){
        cout << ans_index[i] << " ";
    }
    return 0;
}

void KMPSearch(string pat, string txt){
    int M = pat.length();
    int N = txt.length();
    
    computeLPS(pat);
    int i = 0; // index for txt
    int j = 0; // index for pat
    while (i<N){
        if (pat[j]==txt[i]){
            i++;
            j++;
        }else if (pat[j]!=txt[i]){
            if (j!=0){
                j = lps[j - 1];
            }else{
                i++;
            }
        }

        if (j==M){
            ans_index[ans] = i - M+1;
            ans++;
            j = lps[j - 1];
        }
    }
}


void computeLPS(string pat){
    int leng = 0;
    // lps[0]은 항상 0이므로 while문은 i=1부터 시작
    int i = 1;
    while(i<pat.length()){
        if (pat[i]==pat[leng]){
            leng++;
            lps[i] = leng;
            i++;
        }else{
            if (leng!=0){
                leng = lps[leng - 1];
            }else{
                lps[i] = 0;
                i++;
            }
        }
    }
}