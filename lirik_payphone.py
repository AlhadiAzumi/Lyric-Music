import sys
import time

def menjalankan_lirik () :
    lirik = [
        ("\nI'm at a payphone, trying to call home", 0.09),
        ("All of my change I spent on you (oh, oh)", 0.1),
        ("Where have the times gone? baby, it's all wrong", 0.07),
        ("\nWhere are the plans we made for two?", 0.09),
        ("If `Happy Ever After` did exist", 0.098),
        ("I would still be holding you like this", 0.087),
        ("And all those fairy tales are full of shit", 0.09),
        ("\nOne more fucking love song, I'll be sick(uh)", 0.09),
        ("Now I'm at a payphone", 0.089),
    ]

    delay = [0.5, 0.5, 0.36, 1, 1.1, 0.9, 0.67, 0.4, 0.8]
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
