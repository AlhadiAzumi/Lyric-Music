import sys
import time

def menjalankan_lirik () :
    lirik = [
         ("tante......", 0.12),
         ("sudah terbiasa terjadi tante", 0.11),
         ("teman datang ketika lagi butuh saja", 0.1),
         ("coba kalau lagi susah", 0.1),
         ("mereka semua menghilaaaaaaaaang", 0.14),
    ]

    delay = [0.9, 0.6, 0.5, 0.6, 1]
    print("")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate (lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("")

menjalankan_lirik()