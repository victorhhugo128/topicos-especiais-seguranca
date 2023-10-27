import mod_arthmetics
from random import randint

def key_pair_gen(n_bits: int):
    q = mod_arthmetics.find_prime(n_bits)
    print(f"q = {q}")
    g = mod_arthmetics.find_generator(q)
    print(f"g = {g}")
    x = randint(1, q)
    print(f"x = {x}")
    h = mod_arthmetics.exp_mod(g, q, x)
    print(f"h = {h}")
    
    return {'pk': {'q': q, 'g': g, 'h': h}, 'sk': {'x': x, 'q': q}}

def encrypt(pk: dict, m: int):
    print('encrypt')
    rnd = randint(1, pk['q'])
    
    alpha = mod_arthmetics.exp_mod(pk['g'], pk['q'], rnd)
    beta = mod_arthmetics.multiply_mod(m, pk['h']**rnd, pk['q'])
    
    return (alpha, beta)

def decrypt(sk: dict, alpha: int, beta: int):
    k = mod_arthmetics.exp_mod(alpha, sk['q'], sk['x'])
    
    plain = mod_arthmetics.multiply_mod(beta, mod_arthmetics.find_multiplicative_inverse(k, sk['q']), sk['q'])
    print(f"multiply_mod({beta}, {mod_arthmetics.find_multiplicative_inverse(k, sk['q'])}, {sk['q']})")
    
    return plain



if __name__ == '__main__':
    for teste in range(2000):
        key_pair = key_pair_gen(10)
        message = randint(2, key_pair['pk']['q'] - 1)
        
        print(key_pair)
        
        ciphertext = encrypt(key_pair['pk'], message)
        
        plaintext = decrypt(key_pair['sk'], ciphertext[0], ciphertext[1])
        
        print(f"Texto original: {message}\nTexto cifrado = {ciphertext}\nTexto decriptado = {plaintext}\n\n")
        if message != plaintext:
            print("ERRO: MENSAGEM != TEXTO DECRIPTOGRAFADO")
            break