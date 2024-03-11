# 5) Escreva um programa que inverta os caracteres de um string.


# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;


def inverte_string(s):
    if len(s) == 0:
        return s
    else :
        return inverte_string(s[1:]) + s[0]


string = input('Digite uma string: ')
print(inverte_string(string))