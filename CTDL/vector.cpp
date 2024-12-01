#include<iostream>
using namespace std;

int T;

struct Vector {
int size;
int capacity;
T * array;
};

void vecInit(Vector & vec, int initCapacity = 16) {
vec.size = 0; // Ban d?u chua có ph?n t? nào
vec.capacity = initCapacity; // Kh?i t?o dung lu?ng
vec.array = new T[vec.capacity]; // T?o m?ng ch?a ph?n t?
}

void vecDestroy(Vector & vec) {
delete[] vec.array; // Xóa m?ng (gi?i phóng b? nh?)
}

// Sao chép n?i dung t? vec2 sang vec.
void vecCopy(Vector & vec, Vector & vec2) {
	if (&vec != &vec2) { // Ngan c?n t? sao chép
	vec.size = vec2.size; // Ð?t kích thu?c m?i
	vec.capacity = vec2.capacity; // Ð?t dung lu?ng m?i
	delete[] vec.array; // Xóa m?ng cu
	vec.array = new T[vec.capacity]; // T?o m?ng m?i
	// Sao chép các ph?n t? t? vec2 sang vec
	for (int i = 0; i < vec.size; i++)
	vec.array[i] = vec2.array[i];
 }
}
