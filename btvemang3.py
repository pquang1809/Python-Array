m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))

a = []
for i in range(m):
    hang = list(map(int, input(f"Nhap ptu hang {i+1}: ").split()))
    a.append(hang)
print(a)
max = a[0][0]
count = 1
for i in range(m):
    for j in range(n):
        if a[i][j] > max:
            max = a[i][j]
            count = 1
        elif a[i][j] == max:
            count += 1
print("max la: ", max)
print("count =", count)