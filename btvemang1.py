
j = int(input("Nhap so phan tu: "))
mang = []
for i in range(j):
    x = int(input(f"Nhap phan tu thu {i+1}: "))
    mang.append(x)
print("Mang cua ban la: ",  mang)
print("-----------------------------")
max = mang[0]
count = 1
for i in range(1,j):
    if mang[i] > max: # tim min thi lam nguoc lai
        max = mang[i]
        count = 1
    elif mang[i] == max:
        count += 1
print("So lon nhat trong mang nay la: ", max)
print("So lan dem la: ", count)
