import numpy as np #panggil library
def my_bisection(f, a, b, e):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    m = (a + b)/2
    if np.abs(f(m)) < e:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e)

"""**Contoh Pencarian Akar dengan Metode Bagi Dua**

`f(x)=x^2 - 2`
"""

import numpy as np #panggil library
f = lambda x: x**x-2

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))

############# Nomor 1 A ###############

"""`f(x) = x^2 - 2`"""

import numpy as np #panggil library
f = lambda x: x**3-2 *x+1
my_bisection(f, 2, 4, 0.01)
r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))

############# Nomor 1 B ###############

import numpy as np #panggil library
f = lambda x: np.exp(x) - x
my_bisection(f, 2, 4, 0.01)
r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))

############# Nomor 2 A ###############

import numpy as np #panggil library
def my_bisection_iterasi(f, a, b, e, iterasi):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    m = (a + b)/2
    i = 1 #inisialisasi variabel iterasi
    while i < iterasi: #ulangi sampai iterasi mencapai iterasi atau f(m)    mendekati nol
        if np.abs(f(m)) < e:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m #ubah batas bawah menjadi m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m #ubah batas atas menjadi m
        m = (a + b)/2 #hitung titik tengah baru
        i += 1 #tambahkan variabel iterasi
    return m #kembalikan hasil akhir

f = lambda x: x**x-2

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))

############# Nomor 2 B ###############

import numpy as np #panggil library
def my_bisection(f, a, b, e):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    m = (a + b)/2
    if np.abs(f(m)) < e:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e)

#meminta masukan dari user
f_input = input("Masukkan fungsi f(x) dalam bentuk Python: ")
f = lambda x: eval(f_input) #mengubah masukan user menjadi fungsi
a = eval(input("Masukkan batas bawah interval a: ")) #mengubah masukan user menjadi angka
b = eval(input("Masukkan batas atas interval b: ")) #mengubah masukan user menjadi angka
e = eval(input("Masukkan toleransi galat e: ")) #mengubah masukan user menjadi angka

#mencari akar dari f(x) dengan metode bagi dua
r = my_bisection(f, a, b, e)
print("r =", r)
print("f(r) =", f(r))

############# Nomor 2 B ###############

import matplotlib.pyplot as plt #panggil library

#membuat plot dari f(x) dan akarnya
x = np.linspace(a, b, 100) #membuat array x dengan 100 titik antara a dan b
y = f(x) #menghitung nilai f(x) untuk setiap x
plt.plot(x, y, label="f(x)") #membuat garis plot dari f(x)
plt.plot(r, f(r), "ro", label="r") #membuat titik plot dari akar r
plt.axhline(y=0, color="k") #membuat garis horizontal pada y=0
plt.xlabel("x") #memberi label sumbu x
plt.ylabel("f(x)") #memberi label sumbu y
plt.legend() #menampilkan legenda plot
plt.show() #menampilkan plot
