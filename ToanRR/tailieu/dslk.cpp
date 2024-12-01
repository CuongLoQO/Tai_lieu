#include <iostream>
using namespace std;

struct so{
	int n;
	so *tro;
};

so *taonut(int s)
{
	so *q= new so;
	q->n=s;
	q->tro=NULL;
	return q;
}
void taods(so * &l)
{
	l=NULL;
}
void ThemVaoDauDs(so * &l, int s){
	so *p;
	p=taonut(s);
	if(l==NULL){
		l=p;
	}
	else {
		p->tro = l;
		l = p;
	}
}
void ThemVaoCuoiDs(so * &l, so* &c, int s)
{
	so *p;
	p=taonut(s);
	if (l==NULL)
	{
		l=p;
		c=p;
		
	}
	else 
	{
		c->tro=p;
		c=p;
	}
}
void xuat(so *l)
{
	so *h;
	h=l;
	int i=0;
	while (h!=NULL)
	{
		cout<<" "<< h->n;
		i++;
		h=h->tro;
	}
}
int main()
{
	int s, n, x;
	so *l, *c;
	taods(l);
	cout<<"Cho so phan tu n = "; cin>>n;
	for (int i=0; i<n; i++)
	{
		cout<<"Nhap phan tu thu " << i+1<<": "; cin >>s;
		ThemVaoCuoiDs(l, c, s);
	}
	cout <<"Hien thu danh sach:";
	xuat(l);
	cout <<"\nCho x = "; cin >> x;
	cout<<"Hay them x vao dau va cuoi danh sach.";
	cout<<"\nHien thi danh sach:";
	ThemVaoCuoiDs(l,c,x);
	ThemVaoDauDs(l,x);
	xuat(l);
}
