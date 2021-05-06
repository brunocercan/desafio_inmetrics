from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
from Produto.dao_produto import ProdutoDAO, InventarioDAO
from Clientes.dao_cliente import ClienteDAO, EnderecoDAO
from Clientes.models_cliente import Cliente, Endereco
from Produto.models_produto import Produto, Inventario
from functools import wraps
from app_main import app
import jsons
import json

db = MySQL(app)

produto_dao = ProdutoDAO(db)
inventario_dao = InventarioDAO(db)
cliente_dao = ClienteDAO(db)
endereco_dao = EnderecoDAO(db)


#region AUTENTICAÇÃO HTTP BASIC
def login(f):
   @wraps(f)
   def decorated(*args, **kwargs):
      login = request.authorization
      if login and login.username == 'login' and login.password == 'senha':
         return f(*args, *kwargs)
      else:
         return make_response('Login ou senha incorreto!', 401, {'WWW-Authenticate' : 'Basic realm="Necessario Login"'})
   return decorated
#endregion

@app.route('/')
@login
def index():
    return jsonify('index')

#region Produtos

#region Inventario
@app.route('/inventario/buscar/<int:id>')
def inv_listar(id):
      if verifica_id(id):
         inventario = inventario_dao.filtrar_por_id(id)
         a_dict = jsons.dump(inventario)
         return jsonify(a_dict)
      else:
         return jsonify('id cliente invalido!')
      

@app.route('/inventario/cadastrar', methods=['POST'])
def inv_cadastrar():
   id_produto = request.json['id_produto']
   quantidade = request.json['quantidade']
   id_cliente = request.json['id_cliente']
   inventario = Inventario(id_produto, quantidade, id_cliente)
   inventario_dao.salvar(inventario)
   return inv_listar(id_cliente)
#endregion

@app.route('/produtos/listar')
def prod_listar():
   produtos = produto_dao.listar()
   return jsonify(produtos)


@app.route('/produtos/buscar/<int:id>')
def prod_buscar(id):
   if verifica_id_produto(id):
      produto = produto_dao.buscar(id)
      return jsonify(produto)
   else:
      return jsonify('id produto invalido')

   

@app.route('/produtos/cadastrar', methods = ['POST', ])
def prod_cadastrar():
   nome = request.json['nome']
   descricao = request.json['descricao']
   preco = request.json['preco']
   contratacao = request.json['contratacao']
   produto = Produto(nome, descricao, preco, contratacao)
   produto_dao.salvar(produto)
   return jsonify('produto cadastrado com sucesso!')

@app.route('/produtos/alterar/<int:id>', methods =['PUT', ])
def prod_alterar(id):
   nome = request.json['nome']
   descricao = request.json['descricao']
   preco = request.json['preco']
   contratacao = request.json['contratacao']
   produto = Produto(nome, descricao, preco, contratacao, id = id)
   produto_dao.alterar(produto, id)
   return jsonify('produto alterado com sucesso')


@app.route('/produtos/deletar/<int:id>', methods = ['DELETE', ])
def prod_deletar(id):
   if verifica_id_produto(id):
      return produto_dao.deletar(id)
   else:
      return jsonify('id produto invalido')

   


#endregion

#region Clientes

@app.route('/clientes/listar')
@login
def listar():
   lista = cliente_dao.listar()
   a_dict = jsons.dump(lista)
   return jsonify(a_dict)

#region CADASTRAR
@app.route('/clientes/cadastrar', methods=['POST',])
def cadastrar():
   email = request.json['email']
   cpf = request.json['cpf']
   nome = request.json['nome']
   sexo = request.json['sexo']
   cliente = Cliente(email, cpf, nome, sexo)
   cliente_dao.salvar(cliente)
   return jsonify('cliente cadastrado com sucesso!')
#endregion

#region BUSCAR
@app.route('/clientes/buscar/<int:id>')
def buscar(id):
   try:
      cliente = cliente_dao.filtrar_por_id(id)
   except:
      pass
      return jsonify('ID INVALIDO')
   else:
      a_dict = jsons.dump(cliente)
      return jsonify(cliente)
#endregion

#region DELETAR
@app.route('/clientes/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
   if verifica_id(id):
      cliente_dao.deletar(id)
      return jsonify('CLIENTE DELETADO COM SUCESSO!')
   else:
      return jsonify('id invalido')
#endregion

#region ALTERAR
@app.route('/clientes/alterar/<int:id>', methods=['PUT'])
def alterar(id):
   if verifica_id(id):
      cliente = cliente_dao.filtrar_por_id(id)
      nome = request.json['nome']
      email = request.json['email']
      cpf = request.json['cpf']
      sexo = request.json['sexo']
      cliente = Cliente(email, cpf, nome, sexo, id)
      cliente_dao.alterar(cliente, id)
      return jsonify('CLIENTE ALTERADO COM SUCESSO!', jsons.dump(cliente))
   else:
      return jsonify('ID CLIENTE INVALIDO')
   
#endregion

#endregion

#region Enderecos

#region LISTAR
@app.route('/enderecos/listar')
def end_listar():
   lista = endereco_dao.listar()
   return jsonify(jsons.dump(lista))
#endregion

#region BUSCAR
@app.route('/enderecos/buscar/<int:id>')
def end_buscar(id):
   if verifica_id(id):
      lista = endereco_dao.filtrar_por_id(id)
      return jsonify(jsons.dump(lista))
   else:
      return jsonify('id cliente invalido')
#endregion

#region CADASTRAR
@app.route('/enderecos/cadastrar', methods=['POST'])
def end_cadastrar():
   cidade = request.json['cidade']
   estado = request.json['estado']
   logradouro = request.json['logradouro']
   id_cliente = request.json['id_cliente']
   cep = request.json['cep']
   try:
      testa_id_cliente = cliente_dao.filtrar_por_id(id_cliente)
   except:
      pass
      return jsonify('ID CLIENTE INVALIDO')
   else:
      endereco = Endereco(cidade, estado, logradouro, id_cliente, cep)
      endereco_dao.salvar(endereco)
      return jsonify('ENDERECO CADASTRADO COM SUCESSO!', jsons.dump(endereco))
#endregion

#region DELETAR
@app.route('/enderecos/deletar/<int:id>', methods=['DELETE'])
def end_deletar(id):
      endereco_dao.deletar(id)
      return jsonify('ENDEREÇO DELETADO COM SUCESSO')
#endregion

#region ALTERAR
@app.route('/enderecos/alterar/<int:id>', methods=['PUT'])
def end_alterar(id):
   endereco_dao.filtrar_por_id(id)
   cidade = request.json['cidade']
   estado = request.json['estado']
   logradouro = request.json['logradouro']
   id_cliente = request.json['id_cliente']
   cep = request.json['cep']
   endereco = Endereco(cidade, estado, logradouro, id_cliente, cep, id)
   endereco_dao.alterar(endereco, id)
   return jsonify('ENDEREÇO ALTERADO COM SUCESSO!')
#endregion


#endregion

def verifica_id(id):
   try:
      testa_id_cliente = cliente_dao.filtrar_por_id(id)
   except:
      pass
      return False
   else:
      return True

def verifica_id_produto(id):
   try:
      testa_id_produto = produto_dao.buscar(id)
   except:
      pass
      return False
   else:
      return True