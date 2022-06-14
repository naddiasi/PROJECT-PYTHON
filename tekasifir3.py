#Projek Python oleh Cikgu Nurul Naddia dan Cikgu Jaida
#Kuiz Matematik - Hasil Darab Dua Nombor (1 - 10)
#!/usr/bin/env puthon --> this is interpreter line

import random #import function random

ulang = "Y"
kira = 0

while ulang == "Y" :

    #pengisytiharan pemboleh ubah bagi 2 nombor rawak
    x = random.randint(1,10)
    y = random.randint(1,10)

    #Output bagi 2 nombor rawak yang dipilih
    print("Nombor 1 : ", x)
    print("Nombor 2 : ", y)
    print("")

    #coding hasil darab
    hasil_darab = x * y

    jawapan = None

    #coding pengulangan sekiranya jawapan salah
    while jawapan != hasil_darab :
        jawapan = int(input("Hasil Darab Nombor 1 dan Nombor 2 = "))
        
        if jawapan == hasil_darab :
            print("Tahniah! Anda Bijak!!")
            print("")
            break
        else :
            print("Maaf jawapan anda salah! Cuba jawab lagi!!!")
            print("")

    kira = kira + 1
    ulang = input("Masukkan Y untuk teruskan kuiz atau N untuk hentikan kuiz : ")
    print("")

print("\t...Anda telah selesai menjawab kuiz...")
