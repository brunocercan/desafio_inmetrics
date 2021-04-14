from flask import Flask, request, jsonify, make_response
from flask_mysqldb import MySQL
from dao import ClienteDAO, EnderecoDAO
from models import Cliente, Endereco
from functools import wraps
import jsons


app = Flask(__name__)
app.secret_key = 'desafio1'

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

#region CONFIG DB

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "clientes_desafio1"
app.config['MYSQL_PORT'] = 3306

#endregion


db = MySQL(app)
cliente_dao = ClienteDAO(db)
endereco_dao = EnderecoDAO(db)


@app.route('/')
@login
def index():
   return jsonify("index")

#region Rotas Clientes

#region LISTAR
@app.route('/listar')
@login
def listar():
   #flash('Listando Clientes')
   lista = cliente_dao.listar()
   a_dict = jsons.dump(lista)
   return jsonify(a_dict)
#endregion

#region CADASTRAR
@app.route('/cadastrar', methods=['POST',])
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
@app.route('/buscar/<int:id>')
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
@app.route('/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
   cliente_dao.deletar(id)
   return jsonify('CLIENTE DELETADO COM SUCESSO!')
#endregion

#region ALTERAR
@app.route('/alterar/<int:id>', methods=['PUT'])
def alterar(id):
   cliente = cliente_dao.filtrar_por_id(id)
   nome = request.json['nome']
   email = request.json['email']
   cpf = request.json['cpf']
   sexo = request.json['sexo']
   cliente = Cliente(email, cpf, nome, sexo, id)
   cliente_dao.alterar(cliente, id)
   return jsonify('CLIENTE ALTERADO COM SUCESSO!', jsons.dump(cliente))
#endregion

#endregion

#region Rotas Endereco

#region LISTAR
@app.route('/endereco/listar')
def end_listar():
   lista = endereco_dao.listar()
   return jsonify(jsons.dump(lista))
#endregion

#region BUSCAR
@app.route('/endereco/buscar/<int:id>')
def end_buscar(id):
   lista = endereco_dao.filtrar_por_id(id)
   return jsonify(jsons.dump(lista))
#endregion

#region CADASTRAR
@app.route('/endereco/cadastrar', methods=['POST'])
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
@app.route('/endereco/deletar/<int:id>', methods=['DELETE'])
def end_deletar(id):
      endereco_dao.deletar(id)
      return jsonify('ENDEREÇO DELETADO COM SUCESSO')
#endregion

#region ALTERAR
@app.route('/endereco/alterar/<int:id>', methods=['PUT'])
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

app.run(debug=True)   