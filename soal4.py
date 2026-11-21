#program pola segitiga bintang

n = int(input("masukan tinggi segitiga: "))

print("segitiga:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("segitiga terbalik:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()