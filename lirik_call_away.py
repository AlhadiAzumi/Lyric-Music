import sys
import time

def menjalankan_lirik () :
    lirik = [
        ("\nI'm only one", 0.09),
        ("I'm only oneeeeeEeeeEeeeeEeeeeee call away", 0.15),
        ("I'll be there to save the day", 0.14),
        ("\nSuperman got nothing on me", 0.15),
        ("I'm only one call awayyyy", 0.17),
        ("I'm only one call away", 0.178),
    ]

    delay = [1.5, 1.3, 1.2, 1.73, 1.12, 0.8, 0.55, 0.9, 0.8, 1.2]
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate (lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')

    print("\n@alhdzm")

menjalankan_lirik()
