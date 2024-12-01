//Liet ke cac bien so xe dap gom 1 chu cai A hoac D va day 5 chu so.
//Vi du A11403 ; D02238
//Su dung phuong phap sinh cac chinh hop lap chap 5 cua tap hop X (0,1,2,3,4,5,6,7,8,9)
#include<iostream>
using namespace std;
int n=10;
int k=5;
int i;
void incauhinhdau(int *a, int k){
	cout <<"A";
	for(int i=0;i<5;i++){
		cout <<a[i];
	}
	cout <<"\tD";
	for(int i=0;i<5;i++){
		cout <<a[i];
	}
	cout << "\t";
}
void thaythe(int *a, int k, int vt)
{
	for(int i=vt;i<5;i++)
	{
		a[i]=0;
	}
}
void cauhinhtieptheo(int *a, int n, int k)
{
	i=k-1;
	while(i>0)
	{
		if(a[i]==n-1)
			i--;
		if(a[i]<n-1)
		{
			a[i]++;
			thaythe(a,k,i+1);
			incauhinhdau(a,k);
			i=k-1;
		}
	}
	
}

int main(){
	int *a=new int[n];
	for(i=0;i<k;i++)
	{
		a[i]=0;
	}
	incauhinhdau(a,k);
	cauhinhtieptheo(a,n,k);
	system("pause");
}
