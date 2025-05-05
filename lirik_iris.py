import sys
import time

def menjalankan_lirik () :
    lirik = [
        ("\nWhen everything feels like the movies", 0.09),
        ("Yeah, you bleed just to know you're alive", 0.09),
        ("\nAnd I don't want the world to see me", 0.1),
        ("'Cause I don't think that they'd understand", 0.07),
        ("When everything's made to be broken", 0.09),
        ("I just want you to know who i am", 0.12),
    ]

    delay = [0.7, 1.22, 1.27, 1.73, 0.98, 0.8, 0.55, 0.9, 0.8, 1.2]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate (lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print(" ")

menjalankan_lirik()
