# Juridico API (Arquitetura Limpa com Flask)

Este projeto é uma API de um sistema jurídico, seguindo princípios de **Arquitetura Limpa (Clean Architecture)** e utilizando **Flask** como framework web. O objetivo é separar camadas, manter o código organizado e permitir fácil manutenção e escalabilidade.

---

## 🧠 O que é Arquitetura Limpa (Clean Architecture)?

A **Arquitetura Limpa** é um estilo de arquitetura de software que busca separar o código em camadas bem definidas, com dependências direcionadas de fora para dentro. A ideia principal é que as regras de negócio (domínio) não dependam de detalhes externos como frameworks, bancos de dados ou interfaces web.

### 🎯 Princípios principais

- **Independência de Frameworks**
  - Você pode trocar Flask por FastAPI, Django, etc. sem mexer no domínio.
- **Testabilidade**
  - Casos de uso podem ser testados isoladamente sem banco de dados ou HTTP.
- **Independência de UI**
  - O sistema pode ter Web, Mobile, CLI, etc., sem alterar regras de negócio.
- **Independência do Banco de Dados**
  - O domínio não conhece SQLAlchemy, MongoDB ou qualquer banco.
- **Independência de Agentes Externos**
  - Regras de negócio não dependem de bibliotecas externas.

---

## 🧱 Camadas da Arquitetura Limpa no Projeto

A estrutura do projeto segue o padrão abaixo:

```
src/
│
├── domain/                  # Regras de negócio (núcleo)
│   ├── entities/            # Entidades do domínio
│   ├── repositories/        # Interfaces (contratos)
│   ├── exceptions/          # Erros do domínio
│   └── value_objects/       # Objetos de valor
│
├── application/             # Casos de uso (use cases)
│   └── use_cases/
│
├── infrastructure/          # Implementações de infra (detalhes)
│   ├── persistence/
│   │   ├── orm/             # SQLAlchemy (detalhes do DB)
│   │   └── repositories/    # Repositórios concretos
│   ├── security/            # Autenticação e hashing de senha
│   └── web/
│       ├── app/
│       │   ├── controllers/ # Rotas e controllers
│       │   ├── auth/        # JWT e decorators
│       │   └── utils/       # Response padrão
│
└── main.py                  # Inicialização do Flask
```

---

## 🧩 Por que isso é importante?

### ✅ 1. Separação de responsabilidades

Cada camada tem uma responsabilidade:

- **Domain**: regras e validações do negócio.
- **Application**: orquestra os casos de uso.
- **Infrastructure**: tudo que é “detalhe” (DB, API, libs externas).
- **Web**: rotas, controllers, HTTP.

### ✅ 2. Dependências vão de fora para dentro

A regra é simples:

> **camadas externas dependem de camadas internas, mas nunca o contrário.**

Ou seja:

- Repositórios concretos (infra) dependem de interfaces (domain)
- Use cases dependem de interfaces (domain)
- Controllers dependem de use cases

---

## 📌 O que foi implementado hoje

### ✅ 1. Criação das tabelas com Flask-Migrate

Foi configurado o **Flask-Migrate** para criar as tabelas automaticamente no banco SQLite.

---

### ✅ 2. Criação de superusuário via Flask Shell

Foi criado um superusuário diretamente no banco usando o `flask shell` e o repositório de usuários.

---

### ✅ 3. Hash de senha com bcrypt

Foi implementado o `PasswordHasher` usando **bcrypt**, garantindo segurança no armazenamento de senha.

---

### ✅ 4. Padrão de resposta JSON

Foi criada uma classe `ApiResponse` para padronizar todas as respostas da API:

- `code`
- `trace_id`
- `message`
- `data`
- `errors`

E os métodos:

- `success_response()`
- `error_response()`

---

### ✅ 5. Autenticação JWT

Implementado JWT para autenticar rotas:

- Login retorna token JWT
- Rotas protegidas usam `@jwt_required`

---

### ✅ 6. Rotas de Processos

Rotas para:

- Listar processos do usuário logado
- Criar processo (com número único)

Exemplo de rota:

POST /api/processes

GET /api/processes


---

## 🧾 Rotas Disponíveis

### 🔐 Autenticação

#### POST /api/login


---

### 🔐 Autenticação

#### POST /api/login

{
  "email": "<email_do_usuario>",
  "password": "<senha_do_usuario>"
}

> As credenciais devem ser criadas no ambiente local e nunca devem ser armazenadas no repositório.

Retorna:

{
"data": {
"token": "..."
}
}


---

### 📌 Processos

#### GET /api/processes

Retorna lista de processos do usuário logado.

#### POST /api/processes

Cria um novo processo.

Exemplo Body:

```json
{
  "title": "Processo 123",
  "number": "0001234-56.2026.8.26.0100"
}

