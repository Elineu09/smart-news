# API de Autenticação - Documentação

## Endpoints

### 1. Registar Utilizador
**POST** `/api/auth/register`

Cria um novo utilizador.

**Request:**
```json
{
  "nome": "João Silva",
  "email": "joao@example.com",
  "password": "password123"
}
```

**Response (201):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com"
  }
}
```

**Erros:**
- `400` - Dados inválidos ou password muito curta
- `409` - Email já registado

---

### 2. Fazer Login
**POST** `/api/auth/login`

Autentica um utilizador e cria uma sessão.

**Request:**
```json
{
  "email": "joao@example.com",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com"
  }
}
```

**Erros:**
- `401` - Email ou password incorretos

---

### 3. Fazer Logout
**POST** `/api/auth/logout`

Termina a sessão do utilizador.

**Response (200):**
```json
{
  "success": true,
  "message": "Logout realizado com sucesso"
}
```

---

## Configuração de Sessões

As sessões são armazenadas no filesystem (pasta `flask_session/`). 
Para mudar de backend (Redis, Memcached), edite `main.py`:

```python
app.config['SESSION_TYPE'] = 'redis'  # ou 'memcached', 'sqlalchemy'
```

---

## Middleware de Autenticação

Para proteger uma rota, use o decorador `@login_required`:

```python
from app.middleware import login_required
from flask import jsonify

@app.route('/api/user/profile')
@login_required
def profile():
    from app.middleware import get_current_user
    user = get_current_user()
    return jsonify(user), 200
```

---

## Testes

Executar testes das rotas:

```bash
python -m pytest test_auth_routes.py -v
```

---

## Exemplos com cURL

### Registar
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"nome":"João","email":"joao@example.com","password":"password123"}'
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"joao@example.com","password":"password123"}' \
  -c cookies.txt
```

### Logout
```bash
curl -X POST http://localhost:5000/api/auth/logout \
  -b cookies.txt
```
