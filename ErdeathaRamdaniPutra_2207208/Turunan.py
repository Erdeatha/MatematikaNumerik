import numpy as np

def turunan_maju(fungsi, x, h):
    hasil = (fungsi(x + h) - fungsi(x)) / h
    return hasil

def turunan_mundur(fungsi, x, h):
    hasil = (fungsi(x) - fungsi(x - h)) / h
    return hasil

def turunan_tengah(fungsi, x, h):
    hasil = (fungsi(x + h) - fungsi(x - h)) / (2 * h)
    return hasil

input_fungsi = input("Masukkan fungsi: ")
fungsi = lambda x: eval(input_fungsi)

input_nilai_x = input("Masukkan nilai x (pisahkan dengan koma): ")
nilai_x = np.array([float(x) for x in input_nilai_x.split(',')])

input_h = float(input("Masukkan langkah (h): "))

turunan_maju_array = np.vectorize(lambda x: turunan_maju(fungsi, x, input_h))(nilai_x[1:])
turunan_mundur_array = np.vectorize(lambda x: turunan_mundur(fungsi, x, input_h))(nilai_x[:-1])
turunan_tengah_array = np.vectorize(lambda x: turunan_tengah(fungsi, x, input_h))(nilai_x[1:-1])

print(f"\nFungsi: {input_fungsi}")
print(f"Nilai x: {nilai_x}")
print(f"Langkah (h): {input_h}")
print("\nTurunan Pertama (Maju):", turunan_maju_array)
print("Turunan Pertama (Mundur):", turunan_mundur_array)
print("Turunan Pertama (Tengah):", turunan_tengah_array)
