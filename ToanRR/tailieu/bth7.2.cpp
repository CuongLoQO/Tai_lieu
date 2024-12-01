#include <iostream>
using namespace std;

struct date{
	int d, m, y;
};
struct sinhvien{
	string ht;
	date ns;
};
void nhap(sinhvien *p, int n)
{
	for (int i=0; i<n; i++)
	{
		cin.ignore();
		cout<<"Ho ten: "; getline(cin, p[i].ht);
		cout<<"Ngay sinh: "; cin>>p[i].ns.d;
		cout<<"Thang sinh: "; cin>>p[i].ns.m;
		cout<<"Nam sinh: "; cin>>p[i].ns.y;
	}
}
void xuat(sinhvien *p, int n){
	cout<<"-----------Thong tin sinh vien----------\n";
	for(int i=0; i<n;i++){
		cout<<"Ten: "<<p[i].ht <<"---"<<"Nam sinh: "<<p[i].ns.d<<"/"<<p[i].ns.m<<"/"<<p[i].ns.y<<endl;
	}
}
void k(sinhvien *p,int n){
	int k, dem=0;
	cout <<"\n\nNhap nam sinh can tim: "; cin>> k;
	for(int i=0;i<n;i++){
		if(p[i].ns.y==k){
		cout<<"Ten: "<<p[i].ht <<"---"<<"Nam sinh: "<<p[i].ns.d<<"/"<<p[i].ns.m<<"/"<<p[i].ns.y<<endl;
		dem=1;
		}
	}
		if(dem==0) cout<<"Khong co sinh vien sinh nam " << k;
}
void timsv(sinhvien *p,int n){
	int dem=0;
	for(int i=0;i<0;i++){
		if(p[i].ns.d==29&&p[i].ns.m==2)
			dem++;
	}
	if(dem==0)
		cout<<"\nKhong sinh vien sinh ngay 29 thang 2";
	else
		cout<<"\nCo sinh vien sinh ngay 29 thang 2";
		
}
int main()
{
	int n;
	cout<<"Nhap n: ";
	cin>>n;
	sinhvien *p =new sinhvien[n];
	nhap(p, n);
	xuat(p,n);
	k(p,n);
	timsv(p,n);
	delete []p;
	p=NULL;
	return 0;
}
