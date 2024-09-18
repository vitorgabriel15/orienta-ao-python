from modelos.ferramentas import Ferramentas

# Criando instâncias de ferramentas
ferramenta_torna = Ferramentas('Torna', 'Ferro', 'Verde', 'Armazém 1')
ferramenta_chave = Ferramentas('Chave', 'Aço', 'Azul', 'Armazém 2')
ferramenta_sierra = Ferramentas('Sierra', 'Madeira', 'Amarelo', 'Armazém 3')

# Alterando o estado de estoque
ferramenta_torna.alterar_estado()
ferramenta_sierra.receber_preço('Fornecedor A', 30)
ferramenta_sierra.receber_preço('Fornecedor B', 28)
ferramenta_sierra.receber_preço('Fornecedor C', 32)

def main():
    Ferramentas.listar_ferramentas()

if __name__ == '__main__':
    main()
