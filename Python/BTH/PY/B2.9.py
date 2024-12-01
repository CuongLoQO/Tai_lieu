d = int (input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) and (d==29) and (m==2):    
    d_af = 1
    m_af = 3
    y_af = y
    print(d_af, m_af, y_af)
else:
    if (m == 2) and (d <= 28) and (m<12):
        if d == 28:
            d_af = 1
            m_af = m+1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d+1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    elif (m == 4) or (m == 6) or (m == 9) or (m == 11) and (d <= 30) and (m<12):
        if d == 30:
            d_af = 1
            m_af = m+1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d+1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    elif (m == 1) or (m == 3) or (m == 5 )or (m == 7) or (m == 8) or (m == 10) and (d <= 31) and (m<12):
        if d == 31:
            d_af = 1
            m_af = m+1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d+1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    elif (m == 12) and (d <= 31):
        if d == 31:
            d_af = 1
            m_af = 1
            y_af = y
            print(d_af, m_af, y_af)
        else:
            d_af = d+1
            m_af = m
            y_af = y
            print(d_af, m_af, y_af)
    else:
        print("nhap sai")
