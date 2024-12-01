x = int(input("Nhập điểm tb của SV:"))
if x<3.5:
    print("Sv xếp loại yếu")
elif x>=3.5 and x<5:
    print("Sv xếp loại kém")
elif x>=5 and x<6.5:
    print("Sv xếp loại trung bình")
elif x>=6.5 and x<8:
    print("Sv xếp loại khá")
elif x>=8 and x<9:
    print("Sv xếp loại giỏi")
else:
    print("Sv xếp loại xuất sắc")
