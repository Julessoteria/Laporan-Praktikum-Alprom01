import numpy as np

jumlah_pertama = 200000000
jumlah_kedua   = 400000000
bunga_bank     = 0.1
waktu          = 1
tahun          = 0

a = np.log(jumlah_kedua / jumlah_pertama)
b = np.log(1+bunga_bank)

waktu = round(a/b)

print (waktu, "tahun")

