#program deret bilangan dan penjumlahan

n = int(input("masukan n: "))

jumlah_semua = 0
jumlah_genap = 0

print("deret: ", end=" ")

for i in range(1, n + 1):
    print(i, end=" ")

    jumlah_semua = jumlah_genap + i

    if i % 2 == 0:
        jumlah_genap = jumlah_genap + i

print()
print("jumlah semua:", jumlah_semua)
print("jumlah genap:", jumlah_genap)