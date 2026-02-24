import numpy as np
import matplotlib.pyplot as plt

# Öğrenci numaraları
f0 = 24 + 7 + 14   # = 45 Hz

f1 = 45
f2 = 22.5
f3 = 450

fs = 8000  

def make_time(f):
    duration = 3 / f
    return np.arange(0, duration, 1/fs)

def signal(t, f):
    return np.sin(2*np.pi*f*t)

t1 = make_time(f1)
t2 = make_time(f2)
t3 = make_time(f3)

x1 = signal(t1, f1)
x2 = signal(t2, f2)
x3 = signal(t3, f3)

# 3 sinyal
plt.subplot(3,1,1)
plt.plot(t1, x1)
plt.title("f1 = 45 Hz")

plt.subplot(3,1,2)
plt.plot(t2, x2)
plt.title("f2 = 22.5 Hz")

plt.subplot(3,1,3)
plt.plot(t3, x3)
plt.title("f3 = 450 Hz")

plt.tight_layout()
plt.show()

# Toplam sinyal
t = t3
x_sum = signal(t,f1)+signal(t,f2)+signal(t,f3)

plt.plot(t,x_sum)
plt.title("Toplam Sinyal")
plt.show()
