###########################
#Item 1
indice = 13 
soma = 0
k = 0
while k < indice:
    k += 1
    soma += k

print(soma) 
#Saída = 91

###########################
#Item 2
def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_fibonacci(numero))

###########################
#Item 3
"""
a) 1, 3, 5, 7, 9
b) 2, 4, 8, 16, 32, 64, 128
c) 0, 1, 4, 9, 16, 25, 36, 49
d) 4, 16, 36, 64, 100
e) 1, 1, 2, 3, 5, 8, 13
f) 2, 10, 12, 16, 17, 18, 19, 20
"""

###########################
#Item 4
"""
Primeiro eu logaria o primeiro interruptor e esperar alguns minutos. Desligaria o primeiro interruptor e ligar o segundo interruptor, em seguida entrar na sala, então:
Se a lâmpada estiver acesa, o segundo interruptor controla a lâmpada.
Se a lâmpada estiver apagada e ainda estiver fria, então é a lâmpada controlada pelo primeiro interruptor.
Se a lâmpada estiver apagada, mas quente, então o terceiro interruptor controla essa lâmpada.
"""

def inverter_string(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

# Exemplo de uso
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
