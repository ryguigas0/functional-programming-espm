class Produto:
    def __init__(self, id='', preco=0.0, qtd=1):
        self.id = id
        self.preco = preco
        self.qtd = qtd
    def baixar_estoque(self, qtd=1):
        if qtd > 0 and self.qtd > 0:
            self.qtd -= qtd
    def adicionar_estoque(self, qtd=1):
        if qtd > 0:
            self.qtd += qtd

class Pedido:
    def __init__(self, id='', cliente='', pagamento=''):
        self.id = id
        self.cliente = cliente
        self.pagamento = pagamento

class ItemPedido:
    def __init__(self, pedido = Pedido(), produto = Produto(), qtd_produto=1):
        self.pedido = pedido
        self.produto = produto
        self.qtd_produto = qtd_produto
        self.status = 'nao feito'
    def efetuar_pedido(self):
        if self.status != 'efetuado':
            self.produto.baixar_estoque(self.qtd_produto)
            self.status = 'efetuado'
            print(f'Pedido {self.pedido.id} do {self.pedido.cliente} efetuado!')
        else:
            print(f'Pedido {self.pedido.id} já foi efetuado!')

def main():
    prod1 = Produto('abc', 15.5, 30)
    prod2 = Produto('def', 16.3, 20)

    pedido = Pedido('123', 'Roberto', 'cheque')

    item_pedido1 = ItemPedido(pedido, prod1, 10)
    item_pedido2 = ItemPedido(pedido, prod2, 15)

    print(prod1.qtd)
    item_pedido1.efetuar_pedido()
    print(prod1.qtd)
    item_pedido1.efetuar_pedido()
    print(prod1.qtd)

    print(prod2.qtd)
    item_pedido2.efetuar_pedido()
    print(prod2.qtd)
    item_pedido2.efetuar_pedido()
    print(prod2.qtd)

if __name__ == '__main__':
    main()