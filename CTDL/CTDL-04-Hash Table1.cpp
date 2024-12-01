#include <iostream>
#include <string>

using namespace std;

// Muc tu trong tu dien
struct MucTu{
   string tuTiengAnh;
   string nghiaTiengViet;
};

struct TuDien{
   MucTu * table; // Con tro toi bang bam
   int tableSize; // Kich thuoc bang bam, so phan tu        
   bool * trong;  // Neu trong[i] == true thi vi tri i trong bang bam dang trong
};
   
// Ham bam anh xa tu tieng Anh sang mot vi tri trong bang bam:
//   1. Cong cac ky tu
//   2. Chia cho kich thuoc bang bam va lay phan du
int hamBam(string tuTiengAnh, int tableSize){
   int hashVal = 0;
   for(int i = 0; i < tuTiengAnh.size(); i++)
      hashVal += tuTiengAnh[i];
   
   return hashVal % tableSize;
}

// Ham khoi tao tu dien
void KhoiTaoTD(TuDien & td, int size = 101){// Kich thuoc bang bam ngam dinh la 101  
   td.tableSize = size;
   td.table = new MucTu[size];
   td.trong = new bool[size];
   for (int i = 0; i < size; i++)
      td.trong[i] = false;
}

// Ham huy tu dien
void huyTD(TuDien & td){  
   delete [] td.table;
   delete [] td.trong;
}

// Chen muc tu vao tu dien
void chenMucTu(TuDien & td, MucTu mt){  
   int hashVal = hamBam(mt.tuTiengAnh, td.tableSize);
   while (td.trong[hashVal])
      hashVal = (hashVal + 1) % td.tableSize;
   td.table[hashVal] = mt;
   td.trong[hashVal] = true;
}

// Lay nghia tieng Viet
string nghiaTiengViet(TuDien & td, string tuTiengAnh){  
   int hashVal = hamBam(tuTiengAnh, td.tableSize);
   return td.table[hashVal].nghiaTiengViet;
}

// Ham tra ve so muc tu trong tu dien
int CountMT(TuDien & td){
   int count = 0;
   for (int i = 0; i < td.tableSize; i++)
      if (td.trong[i])
         count++;
   return count;
}

// Ham cap nhat nghia tieng Viet cua mot tu tieng Anh
void CapNhatNghia(TuDien & td, string tuTiengAnh, string nghiaTiengViet){
   int hashVal = hamBam(tuTiengAnh, td.tableSize);
   while(td.trong[hashVal] && td.table[hashVal].tuTiengAnh != tuTiengAnh)
      hashVal = (hashVal + 1) % td.tableSize;
   if(td.trong[hashVal])
      td.table[hashVal].nghiaTiengViet = nghiaTiengViet;
}

// Ham kiem tra trung lap tu tieng Anh khi chen muc tu moi vao tu dien
bool CheckTrungLap(TuDien & td, string tuTiengAnh){
   int hashVal = hamBam(tuTiengAnh, td.tableSize);
   while(td.trong[hashVal] && td.table[hashVal].tuTiengAnh != tuTiengAnh)
      hashVal = (hashVal + 1) % td.tableSize;
   if(td.trong[hashVal])
      return true;
   else
      return false;
}

string ChuanHoa(string str){
   for(int i = 0; i < str.size(); i++)
      if(str[i] >= 'a' && str[i] <= 'z')
         str[i] = str[i] - 32;
   return str;
}

// Ham xoa muc tu khoi tu dien
void XoaMucTu(TuDien & td, string tuTiengAnh){
   int hashVal = hamBam(tuTiengAnh, td.tableSize);
   while(td.trong[hashVal] && td.table[hashVal].tuTiengAnh != tuTiengAnh)
      hashVal = (hashVal + 1) % td.tableSize;
   if(td.trong[hashVal])
      td.trong[hashVal] = false;
}

// Ham in ra tu dien
void InRaTuDien(TuDien & td){
   for(int i = 0; i < td.tableSize; i++)
      if(td.trong[i])
         cout << td.table[i].tuTiengAnh << ": " << td.table[i].nghiaTiengViet << endl;
}

int main(){
   TuDien td;
   KhoiTaoTD(td);
   
   // Tao mot vai muc tu
   MucTu mt1, mt2, mt3, mt4, mt5;
   mt1.tuTiengAnh     = "computer";
   mt1.nghiaTiengViet = "may tinh";
   mt2.tuTiengAnh     = "memory";
   mt2.nghiaTiengViet = "bo nho";
   mt3.tuTiengAnh     = "hard disk";
   mt3.nghiaTiengViet = "dia cung";
   mt4.tuTiengAnh     = "hello";
   mt4.nghiaTiengViet = "chao";
   
   // Chen cac muc tu vao tu dien
   chenMucTu(td, mt1);
   chenMucTu(td, mt2);
   chenMucTu(td, mt3);
   chenMucTu(td, mt4);
   chenMucTu(td, mt5);

   string tuTA, nghiaTV;

   // In ra tu dien
   cout << "In tu dien";
   InRaTuDien(td);

   // So muc tu cua tu dien
   cout << "\nSo muc tu hien co cua tu dien la: " << CountMT(td) << endl;

   // Yeu cau nhap tu tieng Anh de tra cuu tu dien
   cout << "\nNhap tu tieng Anh can tra cuu: ";
   getline(cin, tuTA);
   
   // Tim nghia tieng Viet
   nghiaTV = nghiaTiengViet(td, tuTA);
   
   // In ket qua tra cuu
   if(nghiaTV == "")		
      cout << "Tu vua nhap khong co trong tu dien" << endl;
      
   else		
      cout << "Nghia cua tu vua nhap la: " << nghiaTV << endl;

   // Cap nhat nghia tieng Viet
   cout << "\nNhap tu tieng Anh can cap nhat: ";
   getline(cin, tuTA);
   cout << "Nhap nghia tieng Viet cap nhat: ";
   getline(cin, nghiaTV);
   CapNhatNghia(td, tuTA, nghiaTV);
   cout << "Nghia cua tu '" << tuTA << "' sau khi cap nhat la: " << nghiaTiengViet(td, tuTA) << endl;

   cout << "\nIn lai tu dien sau khi cap nhat la";
   InRaTuDien(td);

   // Xoa muc tu
   cout<<"\nXoa muc tu trong tu dien:\n";
   cout << "Nhap tu tieng Anh can xoa: ";
   getline(cin, tuTA);
   XoaMucTu(td, tuTA);

   cout << "\nIn lai tu dien sau khi xoa";
   InRaTuDien(td);
   huyTD(td);
   return 0;
}
