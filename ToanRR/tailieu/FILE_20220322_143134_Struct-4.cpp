#include<iostream>
#include<string>
using namespace std;
struct Sinhvien {
		string ten;
		int  diem;
		Sinhvien *tro;
};	
//Ham tao 1 nut có dulieu = giatri
Sinhvien *Taonut(string t, int d)
{
	Sinhvien  *q = new Sinhvien; 
  	q -> ten = t;
	q-> diem = d;  
  	q -> tro = NULL; 
  	return q;
}   
//Ham khoi tao DS rong
void Taods(Sinhvien * &L)
{
  L = NULL;   
} 
//Ham them 1 nut x vao cuoi DS co con tro dau= L
void Themcuoids(Sinhvien *&L, Sinhvien * &C, string t, int d) 
{
	Sinhvien *p;
	p = Taonut(t,d);
	if (L == NULL) 
	{ L = p;
	  C = p;
	}  
	else 
	{
		C->tro = p;
		C = p;
	}	
}	
//Ham in DS ra man hinh
void Xuatds(Sinhvien *L)
{
	Sinhvien *r; 
	r = L; 
	while (r != NULL)
	{   cout << r->ten << "\t" << r->diem << endl;
		r = r->tro;
	}
}	
//Ham dem cac phan tu la so chan
void Dem8(Sinhvien *L)
{
	int d = 0;
	Sinhvien *r; 
	r = L;
	while (r != NULL) 
	{	if (r->diem >8) d++;
		r= r->tro;
	}	
	if (d==0)cout <<"\nKhong co SV nao co diem >8";
	else cout<< "\nCo " << d<<" SV co diem >8";
}	
//Ham xoa nut con tro p
void Xoa(Sinhvien *&L, Sinhvien * p) 
{
	
	if (L == NULL) 
		cout <<"Khong co nut can xoa"; 
	else 
	{	if (p==L) L=L->tro;
	    else 
		{ Sinhvien *q=L;
		  while (q->tro !=p) q=q->tro;
		  q->tro = p->tro;
		}
		delete p;
	}	
}	
//Ham tim va xoa nut co ten x
void Timxoa(Sinhvien *&L, string x) 
{
	if (L == NULL) cout<<"Khong co SV nao trong DS";
	else 
	{ Sinhvien *r = L;
	  while (r != NULL)
	  {	if (r->ten ==x) Xoa(L,r);
		r = r->tro;
	  }   
	}  
}	
	
int main()
{   int n, d;
	string t,x;
	Sinhvien *L,*C, *p;
	Taods(L);
	cout <<"Nhap so sinh vien n = ";
	cin >> n;
	for (int i=1; i<=n; i++)
	{   cin.ignore();
		cout <<"Nhap ten cua SV thu "<<i<<" : ";
		getline(cin,t);
		cout <<"Nhap diem cua SV thu "<<i<<" : ";
		cin>>d;
		Themcuoids(L,C,t,d);
	}	
	cout<<"Danh sach sinh vien la: \n";
	Xuatds(L);
	Dem8(L);
//	cout<<"\nNhap ten can tim: ";
//	cin.ignore();
//	getline(cin,x);
//	Timxoa(L,x);
//	cout <<"Danh sach sau khi xoa la: \n";
//	Xuatds(L);
}	
