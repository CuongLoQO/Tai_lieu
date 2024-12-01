#include<iostream>
#include<string>

using namespace std;

struct sinhvien{
	int msv;
	string ten;
	string lop;
};
void nhap(sinhvien sv[], int n){
		
		for(int i =0; i<n;i++){
		cin.ignore();
		cout<<"Nhap ten: "; getline(cin,sv[i].ten);
		cout<<"Nhap lop: "; getline(cin,sv[i].lop);
		cout<<"Nhap msv: "; cin>> sv[i].msv;
		}
}
void xuat(sinhvien sv[],int n){
	cout<<"Danh sach sv: \n";
	
	for(int i =0; i<n;i++){
		cout<< "Thong tin sv " << i+1;
		cout<<" Ten: " << sv[i].ten << " -- "<<"Msv: " << sv[i].msv<<" -- "<< "Lop: "<< sv[i].lop << endl;
		}
}
void ttnt(sinhvien sv[], int n){
	cout << "Sinh vien thuoc lop TNTT la: \n";
	for(int i =0; i<n;i++){
		if(sv[i].lop=="TTNT" || sv[i].lop=="ttnt"){
			cout<<" Ten: " << sv[i].ten << " -- "<<"Msv: " << sv[i].msv<<" -- "<< "Lop: "<< sv[i].lop << endl;
		}
	}
}
void sx(sinhvien  sv[],int n){
	for(int i=0;i<n;i++){  
		for(int j=i+1;j<n;j++)
		if( sv[i].ten > sv[j].ten   )
		{
			string t=sv[i].ten;
			sv[i].ten=sv[j].ten;
			sv[j].ten=t;
		}
}
	cout<<"Danh sach ten sv sau khi sap xep: \n";
	for(int i=0;i<n;i++){
		cout<<" Ten: " << sv[i].ten << endl;
		
	}
}
int main(){
	int n;
	cout <<"Nhap so luong sinh vien: "; cin >>n;
	sinhvien sv[n];
	nhap(sv,n);
	xuat(sv,n);
	ttnt(sv,n);
	sx(sv, n);
	return 0;
}