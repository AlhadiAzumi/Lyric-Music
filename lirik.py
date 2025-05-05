import sys
import time

def menjalankan_lirik () :
    lirik = [
         ("So kiss me where I lay down (Ooh-ooh)", 0.1),
         ("My hands pressed to your cheeks", 0.1),
         ("A long way from the playground", 0.12),
         ("I have loved you since we were eighteen", 0.1),
         ("Long before we both thought the same thing", 0.1),
         ("To be loved and to be in love", 0.1),
         ("All I can do is say that these arms were made for holdin' you, oh", 0.11),
         ("I wanna love like you made me feel", 0.1),
         ("When we were eighteen", 0.1),
    ]

    delay = [0.3, 0.7, 0.7, 3.2, 1.2, 0.4, 0.8, 1, 0.7]
    print("\n==18 - One Direction==")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("// Code by Alhadi Azumi")

menjalankan_lirik()
