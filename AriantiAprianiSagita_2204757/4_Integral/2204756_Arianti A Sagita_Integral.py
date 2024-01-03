import numpy as np

def metode_trapesium(fungsi, a, b, n):
    h = (b - a) / n
    hasil = 0.5 * (fungsi(a) + fungsi(b))
    for i in range(1, n):
        hasil += fungsi(a + i * h)
    hasil *= h
    return hasil

def metode_titik_tengah(fungsi, a, b, n):
    h = (b - a) / n
    hasil = 0
    for i in range(n):
        x_tengah = a + (i + 0.5) * h
        hasil += fungsi(x_tengah)
    hasil *= h
    return hasil

def metode_simpson_1per3(fungsi, a, b, n):
    h = (b - a) / n
    hasil = fungsi(a) + fungsi(b)
    for i in range(1, n, 2):
        hasil += 4 * fungsi(a + i * h)
    for i in range(2, n - 1, 2):
        hasil += 2 * fungsi(a + i * h)
    hasil *= h / 3
    return hasil

# Input dari pengguna
persamaan = input("Masukkan persamaan: ")
batas_bawah = float(input("Masukkan batas bawah: "))
batas_atas = float(input("Masukkan batas atas: "))
jumlah_subinterval = int(input("Masukkan jumlah subinterval: "))

# Definisikan fungsi dari persamaan yang dimasukkan
fungsi = lambda x: eval(persamaan, globals(), {'np': np, 'x': x})

# Hitung integral menggunakan metode trapesium
hasil_trapesium = metode_trapesium(fungsi, batas_bawah, batas_atas, jumlah_subinterval)

# Hitung integral menggunakan metode titik tengah
hasil_titik_tengah = metode_titik_tengah(fungsi, batas_bawah, batas_atas, jumlah_subinterval)

# Hitung integral menggunakan metode Simpson 1/3
hasil_simpson = metode_simpson_1per3(fungsi, batas_bawah, batas_atas, jumlah_subinterval)

# Tampilkan hasil
print(f"Hasil Integral (Trapesium): {hasil_trapesium}")
print(f"Hasil Integral (Titik Tengah): {hasil_titik_tengah}")
print(f"Hasil Integral (Simpson 1/3): {hasil_simpson}")
