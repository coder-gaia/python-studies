# FastAPI Task Manager

Projeto desenvolvido para estudo de FastAPI, SQLAlchemy e modelagem relacional. A aplicação implementa uma API REST para gerenciamento de usuários e tarefas, explorando conceitos fundamentais de backend como CRUD, relacionamentos entre entidades, filtros e paginação.

## Tecnologias

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Funcionalidades

### Usuários

- Criar usuário
- Listar usuários
- Buscar usuário por ID
- Atualizar usuário
- Remover usuário
- Buscar usuários por nome
- Paginação de resultados

### Tarefas

- Criar tarefa vinculada a um usuário
- Listar tarefas de um usuário
- Atualizar tarefa
- Remover tarefa
- Marcar tarefa como concluída

## Conceitos estudados

### Modelagem Relacional

Relacionamento **One-to-Many** entre usuários e tarefas.

```text
User
 ├─ id
 ├─ name
 └─ email

Task
 ├─ id
 ├─ title
 ├─ completed
 └─ user_id
```

Um usuário pode possuir múltiplas tarefas, enquanto cada tarefa pertence a apenas um usuário.

### SQLAlchemy Relationships

Utilização de:

- Foreign Keys
- relationship()
- back_populates
- cascade delete

Permite navegar entre entidades de forma intuitiva:

```python
user.tasks
```

```python
task.user
```

### Query Parameters

Busca de usuários por nome:

```http
GET /users?name=alex
```

### Paginação

Listagem paginada de usuários:

```http
GET /users?page=1&limit=10
```

## Endpoints

### Usuários

| Método | Endpoint           | Descrição             |
| ------ | ------------------ | --------------------- |
| GET    | `/users`           | Listar usuários       |
| GET    | `/users/{user_id}` | Buscar usuário por ID |
| POST   | `/users`           | Criar usuário         |
| PUT    | `/users/{user_id}` | Atualizar usuário     |
| DELETE | `/users/{user_id}` | Remover usuário       |

### Tarefas

| Método | Endpoint                    | Descrição                    |
| ------ | --------------------------- | ---------------------------- |
| GET    | `/users/{user_id}/tasks`    | Listar tarefas do usuário    |
| POST   | `/users/{user_id}/tasks`    | Criar tarefa                 |
| PUT    | `/tasks/{task_id}`          | Atualizar tarefa             |
| PATCH  | `/tasks/{task_id}/complete` | Marcar tarefa como concluída |
| DELETE | `/tasks/{task_id}`          | Remover tarefa               |

## Estrutura do Projeto

```text
.
├── main.py
├── models.py
├── schemas.py
├── database.py
├── requirements.txt
└── database.db
```

## Executando o Projeto

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn main:app --reload
```

## Documentação

Acesse a documentação interativa gerada automaticamente pelo FastAPI:

```text
http://127.0.0.1:8000/docs
```

Também disponível em:

```text
http://127.0.0.1:8000/redoc
```

## Aprendizados

Este projeto foi desenvolvido com foco em praticar:

- Desenvolvimento de APIs REST
- FastAPI
- SQLAlchemy ORM
- Pydantic
- Relacionamentos entre entidades
- CRUD completo
- Query Parameters
- Paginação
- Tratamento de erros com HTTPException
- Persistência de dados com SQLite

## Autor

Desenvolvido por Alexandre Gaia para estudos de backend com Python e FastAPI.
