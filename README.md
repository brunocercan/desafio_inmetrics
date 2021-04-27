# Documentação Desafio 1

## Tecnologias Utilizadas:

- Python 3.8.5
- Flask
- MySQL
- PostMan para testes

## Introdução:

### Parte 1

Como foi pedido, desenvolvemos uma API com as funções de Cadastrar, Alterar, Remover e Listar clientes e endereços em um banco de dados, tudo isso com autenticação HTTP Basic.

### Parte 2

API para Catálogo de produtos e Inventário de produtos usando DDD (Domain-Driven Design)

## Modelo do banco de dados:

### Tabela Clientes:

- ID: chave primária para identificação do cliente e uso em funções que necessitam filtrar clientes int not null primary key auto_increment
- email: varchar(30)
- cpf: varchar(11)
- nome: varchar(30)
- sexo: enum('M', 'F')

### Tabela Endereco

- id_endereco: chave primária para identificação do endereco - int not null primary key auto_increment
- cidade: varchar(30)
- estado: varchar(30)
- logradouro: varchar(30)
- id_cliente: chave estrangeira para relacionamento com tabela clientes - int
- cep: varchar(30)

### Tabela Produtos

- id : chave primaria para identificação do produto - int not null primary key auto_increment
- nome : varchar(30)
- descricao: varchar(255)
- preco: decimal(10,2)
- contratacao: enum('S', 'N')

### Tabela inventario

- id_produto: chave estrangeira da tabela produto
- quantidade: int
- id_cliente: chave estrangeira da tabela cliente

## Funções da API:

> Clientes

- Listar (rota /listar)

    Retorna todos os clientes que estão cadastrados no banco de dados.

- Buscar (rota /buscar/id)

    Retorna o cliente com o id informado

- Cadastrar (rota /cadastrar)

    Cadastra um novo cliente no banco de dados. Retorna 'cliente cadastrado com sucesso'

- Alterar (rota /alterar/id)

    Altera os dados de um cliente já cadastrado no banco de dados pelo id. Retorna 'cliente alterado com sucesso' e tabela com as informações do cliente alterado abaixo.

- Deletar (rota /deletar/id)

    Deleta o cliente cadastrado no banco de dados pelo id. Retorna 'cliente deletado com sucesso'

> Endereços

- Listar (rota /endereco/listar)

    Retorna todos os endereços cadastrados no banco de dados.

- Buscar (rota /endereco/buscar/id)

    Retorna todos os endereços cadastrados no id do cliente

- Cadastrar (rota /endereco/cadastrar

    Cadastra um novo endereço no banco de dados

- Alterar (rota /endereco/alterar/id)

    Altera um endereço cadastrado no banco de dados pelo id do endereço

- Deletar (rota /endereco/deletar/id)

    Deleta um endereço cadastrado no banco de dados pelo id do endereço

> Autenticação

- O sistema necessita de autenticação para acesso aos dados. Ao entrar em qualquer rota se você não estiver logado o sistema irá pedir login e senha.

> Produtos

- Listar (rota /produto/listar)

    Retorna todos os produtos que estão cadastrados no banco de dados.

- Buscar (rota /produto/buscar/id)

    Retorna o produto com o id informado

- Cadastrar (rota /produto/cadastrar)

    Cadastra um novo produto no banco de dados. Retorna 'produto cadastrado com sucesso'

- Alterar (rota /produto/alterar/id)

    Altera os dados de um produto já cadastrado no banco de dados pelo id. Retorna 'produto alterado com sucesso' .

- Deletar (rota /produto/deletar/id)

    Deleta o produto cadastrado no banco de dados pelo id. Retorna 'produto deletado com sucesso'

> Inventário

- Buscar (rota /inventario/buscar/id)

    Retorna o inventario do id do cliente inserido na busca.