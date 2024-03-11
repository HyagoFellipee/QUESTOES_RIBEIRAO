import num2words

# 3) Descubra a lógica e complete o próximo elemento:



# a) 1, 3, 5, 7, 9

# b) 2, 4, 8, 16, 32, 64, 128

# c) 0, 1, 4, 9, 16, 25, 36, 49

# d) 4, 16, 36, 64, 100

# e) 1, 1, 2, 3, 5, 8, 13

# f) 2, 10, 12, 16, 17, 18, 19, 200  (números que começam com "d")

def sequencia_a(n):
    for i in range(1, n+1):
        print(2*i-1, end=' ')

def sequencia_b(n):
    for i in range(n):
        print(2**i, end=' ')

def sequencia_c(n):
    for i in range(n):
        print(i**2, end=' ')

def sequencia_d(n):
    for i in range(2, n+2):
        print(i**2, end=' ')

def sequencia_e(n):
    a, b = 1, 1
    print(a, b, end=' ')
    for i in range(n-2):
        a, b = b, a+b
        print(b, end=' ')

def sequencia_f(n):

    count = 0
    number = 2
    while count < n:
        if num2words.num2words(number, lang="pt_BR").startswith("d"):
            print(number, end=' ')
            count += 1
        number += 1

sequencia_a(5)
print()
sequencia_b(8)
print()
sequencia_c(8)
print()
sequencia_d(7)
print()
sequencia_e(7)
print()
sequencia_f(8)






    




