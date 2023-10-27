from random import randint
from math import floor, sqrt

def exp_mod(number: int, modulus: int, exponent: int):
    return number**exponent % modulus

def multiply_mod(n1: int, n2: int, modulus: int):
    mult = n1 * n2
        
    return mult % modulus

def is_relatively_prime(n1: int, n2: int):  # algoritmo de euclides
    if n1 > n2:
        temp = n1
        n1 = n2
        n2 = temp
        
    remainder = 1
    
    while True:    
        remainder = n1 % n2
        if remainder <= 0:
            break
        n1 = n2; n2 = remainder;
        
    if n2 == 1:
        return True
    return False

def find_multiplicative_inverse(n1: int, modulus: int):  # algoritmo de euclides extendido
    n2 = modulus
    
    if n1 > n2:
        temp = n1
        n1 = n2
        n2 = temp
        
    x0 = 1; y0 = 0; x1 = 0; y1 = 1
    
    while True:    
        remainder = n1 % n2
        quotient = n1 // n2
        
        temp_x = x1
        x1 = x0 - quotient * x1
        x0 = temp_x
        
        temp_y = y1
        y1 = y0 - quotient * y1
        y1 = temp_y
        
        if remainder <= 0:
            break
        n1 = n2; n2 = remainder;
        
    return temp_x
    
    
def find_prime(n_bits: int):    # não eficiente para números muito grandes
    while True:
        prime = True
        rand = randint(3, 2**n_bits)
        square_rt = floor(sqrt(rand))
        
        for i in range(2, square_rt + 1):
            if rand % i == 0:
                prime = False
                break
            
        if prime:
            return rand
        
    

def find_generator(modulus: int):
    # tentativas_geradores = set()
    # contador_numeros_grupo = set()
    # tentativas_geradores = 0
    
    soma_grupo = 0
    for elemento in range(1, modulus):
        soma_grupo += elemento
        
    soma_gerador = 0    
    while True:
        rand_n = randint(2, modulus)
        for exponent in range(0, modulus - 1):
            soma_gerador += exp_mod(rand_n, modulus, exponent)
        if soma_grupo == soma_gerador:
            return rand_n
            
        soma_gerador = 0   
            
def find_multiplicative_inverse(number: int, modulus: int):
    for n in range(1, modulus):
        if multiply_mod(number, n, modulus) == 1:
            return n        
    return None
        
            
if __name__ == '__main__':
    # ordem_grupo = 7
    # gerador = find_generator(ordem_grupo)

    # print(f"Gerador = {gerador}")
    # for i in range(0, ordem_grupo - 1):
    #     print(exp_mod(gerador, ordem_grupo, i))
    
    print(is_relatively_prime(10000, 3))
    # ordem_grupo = find_prime(15)
    
    # gerador = find_generator(ordem_grupo)
    
    # ordem_grupo = find_prime(10)
    # rand = randint(1, ordem_grupo)
    
    # print(f"Ordem do Grupo = {ordem_grupo}\nRand = {rand}")
    
    # r = find_multiplicative_inverse(rand, ordem_grupo)
    
    # print(f"X, Y = {r}\nProva = {multiply_mod(rand, r, ordem_grupo)}")
    
            