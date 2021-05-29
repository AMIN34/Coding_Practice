#include<iostream>
#include<vector>
using namespace std;

void print_vector(vector<int>v)
{
     for(int i=0;i<v.size();i++)
     {
         cout<<v[i]<<" ";
     }
     cout<<"\n";
}
int main()
{
    vector<int>v;
    cout<<"size: "<<v.size()<<"\n";
    int n,el;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>el;
        v.push_back(el);
    }
    print_vector(v);
    cout<<"size: "<<v.size()<<"\n";
    print_vector(v);
    v.push_back(6);
    cout<<"size: "<<v.size()<<"\n";
    print_vector(v);
    v.push_back(7);
     print_vector(v);
    cout<<"size: "<<v.size()<<"\n";
    v.pop_back();

     for(auto i =v.begin();i != v.end();i++)
     {
         cout<<*i<<" ";
     }
     cout<<"\n";
     cout<<"size: after delete "<<v.size()<<"\n";
return 0;
}