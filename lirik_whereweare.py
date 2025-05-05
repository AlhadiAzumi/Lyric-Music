import sys
import time

def menjalankan_lirik () :
    lirik = [
        ("\nDid we ever know?", 0.07),
        ("Did we ever know?", 0.07),
        ("Did we ever know?", 0.14),
        ("\nIs it all inside of my head?", 0.09),
        ("Maybe you still think I don't care", 0.07),
        ("But all I need is you", 0.1),
        ("Yeah, you know it's true", 0.05),
        ("Yeah, you know it's true", 0.06),
        ("\nForget about where we are and let go ", 0.1178),
        ("We're so close", 0.07),
    ]

    delay = [0.5, 0.8, 1.76, 1.3, 0.98, 0.8, 0.55, 0.9, 0.8, 1.2]
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
