class Ferramentas:
    ferramentas = []

    def __init__(self, nome, tipo, cor, local):
        self.nome = nome
        self.tipo = tipo
        self.cor = cor
        self.local = local
        self._disponibilidade = False
        Ferramentas.ferramentas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.tipo} | {self.cor} | {self.local} | {self.disponibilidade}'

    @staticmethod
    def listar_ferramentas():
        print('')        
        print(f'{"Nome da ferramenta".ljust(20)} | {"Tipo".ljust(20)} | {"Cor".ljust(20)} | {"Local".ljust(20)} | {"Disponibilidade"}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for ferramenta in Ferramentas.ferramentas:
            print(f'{ferramenta.nome.ljust(20)} | {ferramenta.tipo.ljust(20)} | {ferramenta.cor.ljust(20)} | {ferramenta.local.ljust(20)} | {ferramenta.disponibilidade}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    print('''
          
███████╗███████╗██████╗░██████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░░██████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔════╝
█████╗░░█████╗░░██████╔╝██████╔╝███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░███████║╚█████╗░
██╔══╝░░██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██╔══██║░╚═══██╗
██║░░░░░███████╗██║░░██║██║░░██║██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░██║░░██║██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░

██████╗░██╗░██████╗██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███████╗██╗░██████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗████╗░██║██║██║░░░██║██╔════╝██║██╔════╝
██║░░██║██║╚█████╗░██████╔╝██║░░██║██╔██╗██║██║╚██╗░██╔╝█████╗░░██║╚█████╗░
██║░░██║██║░╚═══██╗██╔═══╝░██║░░██║██║╚████║██║░╚████╔╝░██╔══╝░░██║░╚═══██╗
██████╔╝██║██████╔╝██║░░░░░╚█████╔╝██║░╚███║██║░░╚██╔╝░░███████╗██║██████╔╝
╚═════╝░╚═╝╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░
''')

    @property
    def disponibilidade(self):
        return '❌ indisponível' if self._disponibilidade else '✔️ disponível'

ferramenta_hacha = Ferramentas('Machado', 'Corte', 'Prata', 'Armazém')
ferramenta_pá = Ferramentas('Pá', 'Escavação', 'Preto', 'Jardim')
ferramenta_chave = Ferramentas('Chave Inglesa', 'Ajuste', 'Vermelho', 'Oficina')

Ferramentas.listar_ferramentas()
