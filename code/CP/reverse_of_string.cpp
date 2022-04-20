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
    void rvereseArray(int arr[], int start, int end)
{
	for(;start < end;)
	{
		int temp = arr[start];
		arr[start] = arr[end];
		arr[end] = temp;
		start++;
		end--;
	}
}	
void printArray(int arr[], int size)
{
for (int i = 0; i < size; i++)
cout << arr[i] << " ";
}

    int main()
    {
        FIO;
	    OJ;
	int t=0,end=0;cin>>t;
	for(int i=0;i<t;i++){
		cin>>end;
		}
		int arr[end];
	for(int i=0;i<end;i++){
		cin>>arr[i];
	}
	rvereseArray(arr, 0, end-1);
	printArray(arr, end);
	return 0;
}


