import sys
import time

def menjalankan_lirik () :
    lirik = [
        ("\nI'm looking back on things i've done", 0.12),
        ("I never wanna play the same old part", 0.12),
        ("I'll keep you in the dark", 0.13),
        ("\nNow let me show you", 0.1),
        ("The shape of my heart", 0.07),
        ("looking back on things i've done", 0.1),
        ("I was trying to be someone", 0.12),
        ("\nI played my part", 0.08),
        ("Kept you in the dark", 0.1178),
        ("Now let me show you", 0.09),
        ("The shape of my heart", 0.09),
    ]

    delay = [0.5, 0.9, 1.7, 0.55, 0.5, 0.8, 0.9, 1, 0.8, 1.6, 1.1]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate (lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print(' ')
    print("@alhdzm")

menjalankan_lirik()