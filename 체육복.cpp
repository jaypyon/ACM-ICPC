#include <string>
#include <vector>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    vector<int> count;
    for(int i=0 ;i<n;i++){
        count.push_back(1);
    }
    for(auto i : lost)count[i-1]-=1;
    for(auto i : reserve)count[i-1]+=1;
    
    if(count[0]==0&&count[1]==2){count[0]=1;count[1]=1;}
    for(int i=1; i<n-1;i++){
        if(count[i]==0){
            if(count[i-1]==2){count[i]++;count[i-1]--;}
            else if(count[i+1]==2){count[i]++;count[i+1]--;}
        }
    }
    if(count[n-1]==0&&count[n-2]==2){count[n-1]=1;count[n-2]=1;}
    
    for(auto i : count){
        if(i>0)answer++;
    }
    return answer;
}
