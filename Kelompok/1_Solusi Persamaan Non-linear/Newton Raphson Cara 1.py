# Mendefinisikan fungsi metode newtonRaphson
def newtonRaphson(f, g, x0, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Pembagian dengan nol terjadi')
            break
        # Loop iterasi
        x1 = x0 - f(x0)/g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nAkar yang dibutuhkan : %0.8f' % x1)
    else:
        print('\nTidak konvergen')

# Input fungsi f(x)
expression_f = input("Masukkan fungsi f(x) sebagai contoh x**2-2*x-8: ")
f = lambda x: eval(expression_f)

# Input fungsi g(x)
expression_g = input("Masukkan fungsi g(x) sebagai contoh 2*x-2: ")
g = lambda x: eval(expression_g)

# Convert inputan ke tipe data float
x0 = input('Perkiraan awal: ')
x0 = float(x0)
e = input('Perkiraan Error: ')
e = float(e)
# Convert inputan ke tipe data int
N = input('Jumlah Step: ')
N = int(N)

newtonRaphson(f, g, x0, e, N)
