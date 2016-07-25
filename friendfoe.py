'''program ini akan menampilkan output berupa angka 1 sampai  100.
Namun ketika angka tersebut habis dibagi dengan 4 maka,
outputnya akan berubah menjadi friend, bila habis dibagi 7 berubah menjadi foe dan
akan berubah menjadi friendfoe apabila habis dibagi dengan 4 atau pun 7 '''

import sys
def hitung(i):
    if (i % 4 == 0) and (i % 7 == 0):
        sys.stdout.write("friendfoe")

    elif i % 4 == 0:
        sys.stdout.write("friend")

    elif i % 7 == 0:
        sys.stdout.write("foe")

    else :
        sys.stdout.write(str(i))

#code dibawah berfungsi  untuk menampilkan outputan membentuk baris baru ketika sampai pada angka yang habis dibagi 10
    if i % 10 == 0 :
        sys.stdout.write("\n")

    elif i>0 and i<101 :
        sys.stdout.write(",")

for i in range (1, 101):
    if hitung(i) :
        print (i)

if __name__ == "__hitung__":
    hitung()
