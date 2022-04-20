#include <bits/stdc++.h>
using namespace std;
int main()
{
     int n,k;
    cin>>n>>k;
    int evn[n],odd[n],e=0,o=0;
    vector<  int > t;
    for(int i=1;i<=n;i++){
        if(i%2!=0)
        t.push_back(i);
    }
    for( int i=1;i<=n;i++){
        if(i%2==0)
        t.push_back(i);
    }
    //vector<int>::iterator it;
    //for(int i=0;i<n;i++){
 //  for( it=t.begin();it!=t.end();it++)
    //{
   //     
   cout<<t[k-1]<<endl;
   // }
    


    
//cout<<n<<" "<<k;
    
}