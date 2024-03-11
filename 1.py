# 1) Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);



# Ao final do processamento, qual será o valor da variável SOMA?

# R: 91

soma = 0
indice = 13

for k in range(1, indice+1):
    soma += k

print(soma)

