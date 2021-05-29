#include<iostream>
using namespace std;
long gcd(long int a, long int b){
    if(b==0)
        return a;
    return gcd(b,a%b);
}
long lcm(long int a, long int b){
    return ((a*b)/gcd(a,b));
}
int main(){
    int t,b,c;
    cin>>t;
    while(t--){
        cin>>b>>c;
        cout<<gcd(b,c)<<" "<<lcm(b,c)<<"\n";
    }
}