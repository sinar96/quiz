#program berikut akan menampilkan kapan kita akna berusia 100 tahun

from __future__ import print_function
from datetime import datetime

#Menanyakan nama user
name = str(raw_input("Hay.. What's your name ? \n"))

#Menanyakan umur user
old = int(raw_input("how old are you ? \n"))

now = datetime.now()
toa = now.year - old + 100

print ("you will be 100 years on %i" % toa)
