from __future__ import print_function

bilangan = int(raw_input("Silahkan input bilangan yang akan di cek\n"))

def main():
    if bilangan % 2 == 0 :
        print ("%d merupakan bilangan genap" % bilangan)
    else :
        print ("%d merupakan bilangan ganjil" % bilangan)

if __name__ == "__main__":
    main()
