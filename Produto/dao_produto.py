from Produto.models_produto import Produto, InventarioTupla
from flask import jsonify
import jsons

class ProdutoDAO:
    def __init__(self, db):
        self.__db = db

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute('select id, nome, descricao, preco, contratacao from produtos')
        produtos = converte_produto(cursor.fetchall())
        return produtos

    def buscar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('select id, nome, descricao, preco, contratacao from produtos where id =%s', (id, ))
        tupla = cursor.fetchone()
        return jsons.dump(Produto(id = tupla[0], nome = tupla[1], descricao = tupla[2], preco = tupla[3], contratacao = tupla[4]))

    def salvar(self, produto):
        cursor = self.__db.connection.cursor()
        cursor.execute('insert into produtos (nome, descricao, preco, contratacao) values (%s, %s, %s, %s)', (produto.nome, produto.descricao, produto.preco, produto.contratacao))
        return produto

    def alterar(self, produto, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('update produtos set nome=%s, descricao=%s, preco=%s, contratacao=%s where id = %s', (produto.nome, produto.descricao, produto.preco, produto.contratacao, id))
        return produto

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('delete from produtos where id = %s', (id, ))
        return jsonify('produto deletado com sucesso!')

    


class InventarioDAO:
    def __init__(self, db):
        self.__db = db
    
    def filtrar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('select clientes.nome, clientes.id, produtos.nome, produtos.descricao, produtos.id,\
             inventario.quantidade from produtos inner join inventario on inventario.id_produto = produtos.id \
                  inner join clientes_desafio1.clientes on clientes.id = inventario.id_cliente \
                       where clientes.id = %s', (id, ))
        inventario = cursor.fetchall() 
        return converte_inventario(inventario)


def converte_produto(produtos):
    def cria_produto_com_tupla(tupla):
        return jsons.dump(Produto(id = tupla[0], nome = tupla[1], descricao = tupla[2], preco = tupla[3], contratacao = tupla[4]))
    return list(map(cria_produto_com_tupla, produtos))

def converte_inventario(inventarios):
    def cria_inventario_com_tupla(tupla):
        lista = InventarioTupla(nome = tupla[0], id_cliente= tupla[1], nome_produto=tupla[2], produto_desc=tupla[3], id_produto=tupla[4], quantidade=tupla[5])
        return lista
    return list(map(cria_inventario_com_tupla, inventarios))
