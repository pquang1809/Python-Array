j = int(input("Nhap so phan tu: "))
mang = list(map(int, input("Nhap cac phan tu: ").split()))
print("Mang cua ban la: ", mang)
print("-----------------------------")
x = int(input("Nhap so can check: "))
count = 0 
for i in range(0,j):
    if mang[i] == x:
        count += 1
print(f"So phan tu bang gia tri cua  {x} la:", count)