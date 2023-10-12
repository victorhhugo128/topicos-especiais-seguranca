from mod_arthmetics import * 

class DiffieHellman:
    def __init__(self, ordem_grupo, gerador):
        self.grupo = ordem_grupo
        self.gerador = gerador
        self.param = None
        self.chave_compartilhada = None
        
    def escolher_param_aleatorio(self):
        self.param = randint(1, 10000)
        
    def enviar_parte_da_chave(self):
        return exp_mod(self.gerador, self.grupo, self.param)
    
    def calcular_chave_compartilhada(self, chave_part_enviada):
        self.chave_compartilhada = exp_mod(chave_part_enviada, self.grupo, self.param)
        
        return self.chave_compartilhada
        
        
        
if __name__ == '__main__':
    ordem_grupo = 571
    gerador = find_generator(ordem_grupo)
    
    mensageiro_1 = DiffieHellman(ordem_grupo, gerador)
    mensageiro_2 = DiffieHellman(ordem_grupo, gerador)
    
    # cada mensageiro escolhe um número aleatório para usarem de parâmetro
    mensageiro_1.escolher_param_aleatorio()
    mensageiro_2.escolher_param_aleatorio()
    
    # cada mensageiro calcula a chave compartilhada com o g^p do outro mensageiro
    chave_parte_1 = mensageiro_1.enviar_parte_da_chave()
    mensageiro_2.calcular_chave_compartilhada(chave_parte_1)
    
    chave_parte_2 = mensageiro_2.enviar_parte_da_chave()
    mensageiro_1.calcular_chave_compartilhada(chave_parte_2)
    
    print(f"""Mensageiro 1:
          Ordem do grupo = {mensageiro_1.grupo}
          Gerador = {mensageiro_1.gerador}
          Parâmetro 1 = {mensageiro_1.param}
          Chave Compartilhada = {mensageiro_1.chave_compartilhada}""")
    
    print(f"""Mensageiro 2:
          Ordem do grupo = {mensageiro_2.grupo}
          Gerador = {mensageiro_2.gerador}
          Parâmetro 2 = {mensageiro_2.param}
          Chave Compartilhada = {mensageiro_2.chave_compartilhada}""")
    
    
    
        
    