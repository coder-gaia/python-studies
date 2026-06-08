# FastAPI Task Manager

Projeto desenvolvido para estudo de FastAPI, SQLAlchemy, modelagem relacional e testes automatizados.

A aplicação implementa uma API REST para gerenciamento de usuários e tarefas, explorando conceitos fundamentais de backend como CRUD, relacionamentos entre entidades, injeção de dependência, persistência de dados e testes de API.

## Tecnologias

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- HTTPX / TestClient

---

## Funcionalidades

### Usuários

- Criar usuário
- Listar usuários
- Buscar usuário por ID
- Atualizar usuário
- Remover usuário
- Buscar usuários por nome

### Tarefas

- Criar tarefa vinculada a um usuário
- Listar tarefas de um usuário
- Atualizar tarefa
- Remover tarefa
- Marcar tarefa como concluída

### Testes Automatizados

- Teste de criação de usuário
- Teste de busca de usuário
- Teste de usuário inexistente
- Teste de atualização de usuário
- Teste de remoção de usuário
- Teste de criação de tarefa
- Teste de listagem de tarefas
- Teste de atualização de tarefa
- Teste de conclusão de tarefa
- Teste de remoção de tarefa

---

## Conceitos Estudados

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

Um usuário pode possuir múltiplas tarefas.

Cada tarefa pertence a apenas um usuário.

---

### SQLAlchemy Relationships

Utilização de:

- Foreign Keys
- relationship()
- back_populates
- cascade delete

Permite navegar entre entidades sem escrever consultas SQL manualmente.

```python
user.tasks
```

Retorna todas as tarefas do usuário.

```python
task.user
```

Retorna o usuário dono da tarefa.

---

### Dependency Injection com FastAPI

Uso do sistema de dependências do FastAPI para gerenciamento automático das sessões do banco.

```python
db: Session = Depends(get_db)
```

Benefícios:

- Código mais limpo
- Menos repetição
- Fechamento automático das sessões
- Facilita testes automatizados

---

### Query Parameters

Filtro por nome:

```http
GET /users?name=alex
```

---

### Schemas com Pydantic

Validação automática dos dados recebidos pela API.

```python
class UserCreate(BaseModel):
    name: str
    email: str
```

Benefícios:

- Validação automática
- Documentação automática
- Tipagem forte
- Menos código manual

---

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

---

## Estrutura do Projeto

```text
.
├── main.py
├── models.py
├── schemas.py
├── database.py
├── requirements.txt
├── database.db
│
└── tests
    ├── test_users.py
    └── test_tasks.py
```

---

## Executando o Projeto

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Executando os Testes

Ative o ambiente virtual:

```bash
.\.venv\Scripts\activate
```

Execute os testes:

```bash
python -m pytest
```

Saída esperada:

```text
10 passed
```

---

## Documentação

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Aprendizados

- Desenvolvimento de APIs REST
- FastAPI
- SQLAlchemy ORM
- Pydantic
- Relacionamentos entre entidades
- CRUD completo
- Dependency Injection
- Query Parameters
- Tratamento de erros com HTTPException
- Persistência de dados com SQLite
- Testes automatizados com Pytest
- Testes de endpoints HTTP com TestClient

---

## Autor

Desenvolvido por **Alexandre Gaia** para estudos de backend com Python, FastAPI e testes automatizados.
