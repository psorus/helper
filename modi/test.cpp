#include <iostream>
#include <cmath>
using namespace std;


long qmm(long alpha,long beta,long a,long b){
    auto x=alpha;
    long mode=a*b;
    while(x%b!=beta){x=(x+a)%(mode);}
    return x;
}

int main(){
    for(int i=0;i<3;++i){
        for(int j=0;j<5;++j){
            cout<<qmm(i,j,3,5)<<endl;
        }
    }
    return 1;
}
