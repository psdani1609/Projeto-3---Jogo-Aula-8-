class Jogo:
    def __init__(self, id_jogo, titulo, console, genero, publisher, developer, critic_score, total_vendas, vendas_an, vendas_jp, vendas_eu, outras_vendas, data_lanc):
        self.id_jogo       = id_jogo
        self.titulo        = titulo
        self.console       = console
        self.genero        = genero
        self.publisher     = publisher
        self.developer     = developer
        self.critic_score  = critic_score
        self.total_vendas  = total_vendas
        self.vendas_an     = vendas_an
        self.vendas_jp     = vendas_jp
        self.vendas_eu     = vendas_eu
        self.outras_vendas = outras_vendas
        self.data_lanc     = data_lanc

class FilaBackLog:
    def __init__(self):
        self.dados = []

    def enqueue(self, jogo):
        self.dados.append(jogo)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.dados.pop(0)
    
    def is_empty(self):
        return len(self.dados) == 0
    
    def mostrar(self):
        if self.is_empty():
            print('Backlog vazio')
            return
        for i, jogo in enumerate(self.dados, start=1):
            print(f'ID: {i}')
            jogo.exibir()

    def tamanho(self):
        return len(self.dados)

    def contem(self, id):
        for jogo in self.dados:
            if jogo.id == id:
                return True
        return False
             
class PilhaRecentes:
    def __init__(self, limite = 20):
        self.dados = []
        self.limite = limite

    def push(self,jogo):
        indice = -1
        for i in range(len(self.dados)):
            if self.dados[i].id == jogo.id:
                indice = i
                break
        
        if indice != -1:
            self. dados.pop(0)

        self.dados.append(jogo)
        if len(self.dados) > self.limite:
            self.dados.pop(0)

    def pop(self):
        if self.is_empty():
            return None
        return self.dados.pop()
    
    def topo(self):
        if self.is_empty():
            return None
        return self.dados[-1]
    
    def is_empty(self):
        return len(self.dados) == 0
    
    def tamanho(self):
        return len(self.dados)
    
    def mostrar(self):
        for i in range(len(self.dados)-1, -1, -1):
            self.dados[i].exibir()