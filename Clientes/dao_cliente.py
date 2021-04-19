from Clientes.models_cliente import Cliente, Endereco
from flask import jsonify
import jsons

class ClienteDAO:
    def __init__(self, db):
        self.__db = db
    
    def salvar(self, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute('INSERT into clientes (email, cpf, nome, sexo) values (%s, %s, %s, %s)', (cliente.email, cliente.cpf, cliente.nome, cliente.sexo))
        cliente.id = cursor.lastrowid
        self.__db.connection.commit()
        return cliente
    
    def alterar(self, cliente, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('UPDATE clientes SET email=%s, cpf=%s, nome=%s, sexo=%s where id = %s', (cliente.email, cliente.cpf, cliente.nome, cliente.sexo, id))
        return jsonify('Cliente alterado com sucesso!')

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute('SELECT id, email, cpf, nome, sexo from clientes')
        clientes = converte_cliente(cursor.fetchall())
        return clientes
    
    def filtrar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('SELECT id, email, cpf, nome, sexo from clientes where id=%s', (id, ))
        tupla = cursor.fetchone()
        return jsons.dump(Cliente(id=tupla[0], nome=tupla[3], email=tupla[1], cpf=tupla[2], sexo=tupla[4]))

    def deletar(self, id):
        self.__db.connection.cursor().execute('delete from clientes where id = %s', (id, ))
    

class EnderecoDAO:
    def __init__(self, db):
        self.__db = db

    def filtrar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('SELECT id_endereco, cidade, estado, logradouro, id_cliente, cep from endereco where id_cliente = %s', (id, ))
        lista = converte_endereco(cursor.fetchall())
        return lista

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute('SELECT id_endereco, cidade, estado, logradouro, id_cliente, cep from endereco')
        enderecos = converte_endereco(cursor.fetchall())
        return enderecos
    
    def salvar(self, endereco):
        cursor = self.__db.connection.cursor()
        cursor.execute('INSERT INTO endereco (cidade, estado, logradouro, id_cliente, cep) values (%s, %s, %s, %s, %s)', (endereco.cidade, endereco.estado, endereco.logradouro, endereco.id_cliente, endereco.cep))
        endereco.id_endereco = cursor.lastrowid
        self.__db.connection.commit()
        return endereco

    def deletar(self, id):
        self.__db.connection.cursor().execute('delete from endereco where id_endereco = %s', (id, ))

    def alterar(self, endereco, id):
        cursor = self.__db.connection.cursor()
        cursor.execute('UPDATE endereco SET cidade=%s, estado=%s, logradouro=%s, id_cliente=%s, cep=%s where id_endereco=%s', (endereco.cidade, endereco.estado, endereco.logradouro, endereco.id_cliente, endereco.cep, id))
        return endereco
    



def converte_cliente(clientes):
    def cria_cliente_com_tupla(tupla):
        a_dict = jsons.dump(Cliente(id=tupla[0], email=tupla[1], cpf=tupla[2], nome=tupla[3], sexo=tupla[4]))
        return a_dict #ordenando as tuplas em id, nome, email, cpf e sexo   
    return list(map(cria_cliente_com_tupla, clientes))

def converte_endereco(enderecos):
    def cria_endereco_com_tupla(tupla):
        return jsons.dump(Endereco(id_endereco=tupla[0], cidade=tupla[1], estado=tupla[2], logradouro=tupla[3], id_cliente=tupla[4], cep=tupla[5]))
    return list(map(cria_endereco_com_tupla, enderecos))