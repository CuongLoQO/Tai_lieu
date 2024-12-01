#include<iostream>
#include<string>
using namespace std;
struct sinhvien {
	string ten;
	int namsinh;
	string msv;
	sinhvien* next;
};
sinhvien* taosv(string ten,int namsinh,string msv) {
	sinhvien* p = new sinhvien;
	p->msv = msv;
	p->namsinh = namsinh;
	p->ten = ten;
	p->next = NULL;
	return p;
}
void themvaodau(sinhvien* &head,sinhvien * p) {
	if (head == NULL) {
		head = p;
	}
	else
		p->next = head;
		head = p;
}
void themvaocuoi(sinhvien* &head,sinhvien * &tail,sinhvien * p) {
	cin.ignore();
	if (head == NULL) {
		head = tail = p;
	}
	else {
		tail->next = p;
		tail = p;
	}
		
}
//void nhap() {
//	string msv;
//	int namsinh;
//	string ten;
//	while (1) {
//		cout << "Nhap MaSV: "; getline(cin, msv);
//		if (msv == "") break;
//		cout << "Nhap ten: "; getline(cin, ten);
//		cout << "Nam sinh: "; cin >> namsinh;
//		
//	}
//}
void xuat(sinhvien* head) {
	cout << "Hien thi danh sach:\n";
	for (sinhvien* p = head; p != NULL; p = p->next) {
		cout << p->msv << "\t" << p->ten << "\t" << p->namsinh << endl;
	}
}

int main() {
	sinhvien* head = new sinhvien;
	head = NULL;
	sinhvien* tail = new sinhvien;
	tail = NULL;
	string msv;
	int namsinh;
	string ten;
	while (1) {
		cout << "Nhap MaSV: "; getline(cin, msv);
		if (msv == "") {
			break;
		}
		
		cout << "Nhap ten: "; getline(cin, ten);
		cout << "Nam sinh: "; cin >> namsinh;
		themvaocuoi(head, tail, taosv(ten, namsinh, msv));
		//cin.ignore();
	}
	xuat(head);
	cout << "Cho SV can them vao dau DS:\n";
	cin.ignore();
	cout << "MaSV: "; getline(cin, msv);
	cout << "Ten: "; getline(cin, ten);
	cout << "Nam sinh: "; cin >> namsinh;
	themvaodau(head, taosv(ten, namsinh, msv));
	xuat(head);
	return 0;
}
