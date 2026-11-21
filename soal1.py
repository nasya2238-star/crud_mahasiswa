#program menentukan bilangan

bilangan = int(input("masukan bilangan: "))

#menentukan positif, negatif, atau nol
if bilangan > 0:
    print("bilangan positif")
elif bilangan < 0:
    print("bilangan negatif")
else :
    print("bilangan nol")

#menentukan ganjil atau genap
if bilangan != 0:
    if bilangan % 2 == 0:
        print("bilangan genap")
    else :
        print("bilangan ganjil")