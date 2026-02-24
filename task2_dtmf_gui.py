import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import tkinter as tk

FS = 8000
DURATION = 0.3

DTMF = {
    "1": (697,1209), "2": (697,1336), "3": (697,1477),
    "4": (770,1209), "5": (770,1336), "6": (770,1477),
    "7": (852,1209), "8": (852,1336), "9": (852,1477),
    "*": (941,1209), "0": (941,1336), "#": (941,1477),
}

def play(key):
    f1,f2 = DTMF[key]
    t = np.arange(0,DURATION,1/FS)
    x = 0.5*(np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t))
    sd.play(x,FS)

    plt.plot(t,x)
    plt.title(f"{key} Tuşu ({f1}Hz + {f2}Hz)")
    plt.show()

root = tk.Tk()
root.title("DTMF")

for key in DTMF.keys():
    tk.Button(root,text=key,width=5,height=2,
              command=lambda k=key: play(k)).pack()

root.mainloop()
