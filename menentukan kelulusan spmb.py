#program menentukan kelulusan spmb

a = float(input("masukan nilai matematika: "))
b = float(input("masukan nilai bahasa inggris: "))
c =float(input("masukan nilai bahasa indonesia: "))

#proses
nilai = (a + b + c ) / 3

if nilai >= 85 :
    print("lulus")
elif nilai >= 75 :
    print("tidak lulus")
else:
    print("perlu diperbaiki")