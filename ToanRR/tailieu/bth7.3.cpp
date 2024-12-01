#include<iostream>

using namespace std;

struct so{
	int data;
	so *next;
};
so *themso(int dulieu){
	so *p= new so;
	p->data=dulieu;
	p->next=NULL;
	return p;
}
void taods(so * &L){
	L=NULL;
}
void themsovaocuoi(so * &L, so * &C, int x){
	so *p;
	p=themso(x);
	if(L==NULL){
		L=p;
		C=p;
	}
	else{
		C->next=p;
		C=p;
	}
}
void xuat(so *L){
	so *h;
	h=L;
	while(h!=NULL){
		cout<< h->data<<endl;
		h=h->next;
	}
}
int main(){
	int n,x;
	do{
		cout <<"Nhap n: "; cin>>n;
	} while(n<5);
	so *L,*C,*p;
	taods(L);
	for(int i=0;i<n;i++){
		cout << "Nhap so thu " << i+1<<": "; cin>>x;
		themsovaocuoi(L,C,x);
	}
	cout << "Danh sach da nhap la: ";
	xuat(L);
	return 0;
	
}
