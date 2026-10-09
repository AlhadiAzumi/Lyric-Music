import sys
import time

def menjalankan_lirik () :
    lirik = [
        ("\nkita hampir mati dan kau sеlamatkan aku", 0.12),
        ("dan ku menyelamatkanmu dan sekarang aku tahu", 0.12),
        ("\ncеrita kita tak jauh berbeda", 0.16),
        ("got beat down by the world", 0.12),
        ("sometimes I wanna fold", 0.09),
        ("\nnamun suratmu kan kuceritakan ke anak-anakku nanti", 0.1),
        ("bahwa aku pernah dicintai", 0.16),
        ("everything u are", 0.19),

    ]

    delay = [0.7, 0.7, 1, 0.8, 1, 0.8, 0.8, 0.9, 0.8, 0.7]
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
