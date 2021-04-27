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

| Coluna    | Tipo |
|-------|-----------------------------------|
| id | INT, AUTO_INCREMENT, NOT NULL PK                  |
| email | VARCHAR(30)                       |
| cpf   | VARCHAR(11)                       |
| nome  | VARCHAR(30)                       |
| sexo  | ENUM('M', 'F')                    |

### Tabela Endereco

| Coluna      | Tipo                              |
|-------------|-----------------------------------|
| id_endereco | INT, AUTO_INCREMENT, NOT NULL, PK |
| cidade      | VARCHAR(30)                       |
| estado      | VARCHAR(30)                       |
| logradouro  | VARCHAR(30)                       |
| id_cliente  | FK                                |
| cep         | VARCHAR(30)                       |

### Tabela Produtos

| Coluna      | Tipo                              |
|-------------|-----------------------------------|
| id          | INT, AUTO_INCREMENT, NOT NULL, PK |
| nome        | VARCHAR(30)                       |
| descricao   | VARCHAR(255)                      |
| preco       | DECIMAL(10,2)                     |
| contratacao | ENUM('S', 'N')                    |

### Tabela inventario

| Coluna     | Tipo |
|------------|------|
| id_produto | FK   |
| quantidade | INT  |
| id_cliente | FK   |

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