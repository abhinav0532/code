#include <iostream>
#include <string>
using namespace std;
#define ll long long
#define OJ                            \
    freopen("input.txt", "r", stdin); \
    freopen("output.txt", "w", stdout);
#define FIO                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
    
    int main()
    {
        FIO;
	    OJ;
        string s;
        int count=0;
        cin>>s;
       // cout<<s.size()<<endl;
        for(int j=0;j<s.size();j++){
        for(int i=j+1;i<s.size();i++)
        {
            if(s[j]==s[i])
           {  count++;
               break;}
        
        }

    }
    //cout<<"count "<<count<<endl;
    if((s.size()-count)%2==0)
    cout<<"CHAT WITH HER!"<<endl;
    else
    cout<<"IGNORE HIM!"<<endl;
    }