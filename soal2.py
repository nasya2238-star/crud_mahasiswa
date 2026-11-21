#program konversi nilai ke grade

nilai = int(input("masukan nilai: "))

if nilai < 0 or nilai > 100:
    print("nilai tidak valid")
elif nilai >= 85:
    print("grade: a")
elif nilai >= 70:
    print("grade: b")
elif nilai >= 65:
    print("grade: c")
else:
    print("grade: d")