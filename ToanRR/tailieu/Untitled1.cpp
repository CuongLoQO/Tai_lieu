#include <bits/stdc++.h>
using namespace std;
const char ginp[]="DT.INP";
int a[101][101]; //Ma trận kề biểu diễn đồ thị
int n, v, s;
int cx[101]; //Mảng đánh dấu các đỉnh chưa xét
void init()
{ freopen(ginp, "r", stdin);
//Doc du lieu vao
cin>>n;
for (int i=1; i<=n; i++)
for (int j=1; j<=n; j++) cin>>a[i][j];
//Khoi tao các dinh deu chua tham
for (int i = 1; i <= n; i++) cx[i] = 0;
cout<<"So dinh: "<<n<<"\n";
cout<<"Ma tran ke cua do thi:"<<"\n";
for (int i=1; i<=n; i++)
{ for (int j=1; j<=n; j++) cout<<a[i][j]<<" ";
cout<<"\n"; }
}
void DFS(int u)
{ 	cout << u <<" "; cx[u] = 1; //đánh dấu đỉnh u đã thăm.
	for (int v = 1; v <= n; v++)
		if (a[u][v] == 1 && cx[v]==0) DFS(v);
	 }//nếu v kề u và v chưa thăm thì gọi DFS(v)
int main(){ 	
	init(); s=1; cout<<"Duyet theo chieu sau bat dau tu dinh: "<<s<<"\n";
	DFS(s); return 0;
 }
1