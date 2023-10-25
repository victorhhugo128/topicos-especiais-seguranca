from mod_arthmetics import *
from random import randint

def key_pair_gen(n_bits: int):
    p = find_prime(n_bits)
    q = find_prime(n_bits)
    
    
    n = p * q
    totient = (p - 1) * (q - 1)
    
    relative_prime = False
    while not relative_prime:
        e = randint(2, totient)
        relative_prime = is_relatively_prime(totient, e)
        
    d = find_multiplicative_inverse(e, totient)
    
    return {'pk': {'e': e, 'n': n}, 'sk': {'d': d, 'n': n}}

def encrypt(pk: dict, m: int):
    cipher = exp_mod(m, pk['n'],pk['e'])
    
    return cipher

def decrypt(sk: dict, c: int):
    plain = exp_mod(c, sk['n'], sk['d'])
    
    return plain


if __name__ == '__main__':
    key_pair = key_pair_gen(10)
    message = randint(1, key_pair['pk']['n'])
    
    ciphertext = encrypt(key_pair['pk'], message)
    
    plaintext = decrypt(key_pair['sk'], ciphertext)
    print(key_pair)
    
    print(f"Texto original: {message}\nTexto cifrado = {ciphertext}\nTexto decriptado = {plaintext}")