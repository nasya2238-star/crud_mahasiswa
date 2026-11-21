#program bilangan prima dalam rentang

bawah = int(input("batas bawah: "))
atas = int(input("batas atas: "))

jumlah = 0

print("bilangan prima:", end=" ")

for angka in range(bawah, atas + 1):
    if angka > 1:
        prima = True

        for pembagi in range(2, angka):
            if angka % pembagi == 0:
                prima = False
                break

        if prima:
            print(angka, end=" ")
            jumlah = jumlah + 1

print()
print("jumlah:", jumlah)