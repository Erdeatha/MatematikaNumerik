# Import library yang dibutuhkan
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan menu
def menu():
  print("Pilih metode interpolasi yang ingin digunakan:")
  print("1. Metode Lagrange")
  print("2. Metode Newton")
  print("3. Metode Newton Gregory")
  pilihan = input("Masukkan pilihan Anda (1/2/3): ")
  return pilihan

# Fungsi untuk menghitung interpolasi Lagrange
def interpolasi_lagrange(x, y, x_baru):
  # Inisialisasi polinomial interpolasi
  p_lagrange = np.zeros(len(x))

  # Looping untuk menghitung koefisien polinomial interpolasi
  for i in range(len(x)):
    p_lagrange[i] = 1
    for j in range(len(x)):
      if i != j:
        p_lagrange[i] *= (x_baru - x[j]) / (x[i] - x[j])

  # Mengembalikan nilai interpolasi
  return p_lagrange.dot(y)

# Fungsi untuk menghitung interpolasi Newton
def interpolasi_newton(x, y, x_baru):
  # Inisialisasi polinomial interpolasi
  p_newton = np.zeros(len(x))

  # Looping untuk menghitung koefisien polinomial interpolasi
  for i in range(len(x)):
    p_newton[i] = y[i]
    for j in range(i - 1, -1, -1):
      p_newton[j] = p_newton[j] - p_newton[i] * (x[j] - x[i]) / (x[i] - x[j - 1])

  # Mengembalikan nilai interpolasi
  return p_newton[0]

# Fungsi untuk menghitung interpolasi Newton Gregory
def interpolasi_newton_gregory(x, y, x_baru):
  # Inisialisasi polinomial interpolasi
  p_newton_gregory = np.zeros(len(x))

  # Looping untuk menghitung koefisien polinomial interpolasi
  for i in range(len(x)):
    p_newton_gregory[i] = y[i]
    for j in range(1, i + 1):
      p_newton_gregory[i] = p_newton_gregory[i] - p_newton_gregory[i - j] * (x[i] - x[i - j]) / (x[i] - x[i - j - 1])

  # Mengembalikan nilai interpolasi
  return p_newton_gregory[0]

# Fungsi utama
def main():
  # Menerima inputan data
  x = np.array([1, 2, 3])
  y = np.array([2, 4, 6])
  x_baru = float(input("Masukkan nilai x yang ingin diinterpolasi: "))

  # Menampilkan menu
  pilihan = menu()

  # Menghitung interpolasi
  if pilihan == "1":
    f_baru = interpolasi_lagrange(x, y, x_baru)
  elif pilihan == "2":
    f_baru = interpolasi_newton(x, y, x_baru)
  elif pilihan == "3":
    f_baru = interpolasi_newton_gregory(x, y, x_baru)

  # Menampilkan hasil interpolasi
  print("Nilai interpolasi:", f_baru)

  # Visualisasi data
  plt.plot(x, y, "bo")
  plt.plot([x_baru], [f_baru], "ro")
  plt.grid()
  plt.show()

if __name__ == "__main__":
  main()
