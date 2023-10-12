from random import randint

def exp_mod(number: int, modulus: int, exponent: int):
    return number**exponent % modulus

def find_generator(modulus: int):
    tentativas_geradores = set()
    contador_numeros_grupo = set()
    
    while True:
        rand_n = randint(2, modulus)
        
        if rand_n not in tentativas_geradores:
            for exponent in range(0, modulus - 1):
                nova_geracao = exp_mod(rand_n, modulus, exponent)
                if nova_geracao in contador_numeros_grupo:
                    tentativas_geradores.add(rand_n)
                    break
                contador_numeros_grupo.add(nova_geracao)
                if len(contador_numeros_grupo) == (modulus - 1):
                    # print(f"len(contador_numeros_grupo) = {len(contador_numeros_grupo)}\n")
                    return rand_n
            contador_numeros_grupo = set()
            
        
            
if __name__ == '__main__':
    ordem_grupo = 7
    gerador = find_generator(ordem_grupo)

    print(f"Gerador = {gerador}")
    for i in range(0, ordem_grupo - 1):
        print(exp_mod(gerador, ordem_grupo, i))
            