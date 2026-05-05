# Projeto: Smart News

## Pilha Técnica
- Frontend: HTML + CSS + JavaScript (Vanilla)
- Backend: Flask (Python)
- Banco de Dados: SQLite
- API externa: API pública de notícias (REST)

Restrições:
- Não usar React
- Não usar TypeScript
- Não usar frameworks frontend

---

## Padrões de Codificação
- O sistema deve utilizar JavaScript puro (ES6+)
- O código deve ser claro, modular e reutilizável
- Funções devem ter responsabilidade única
- Evitar duplicação de código (DRY)
- Utilizar nomes descritivos para variáveis e funções

---

## Princípios de Arquitectura
- Separar claramente:
  - UI (frontend)
  - Lógica de negócio (backend)
  - Acesso a dados (base de dados)

- O sistema deve seguir arquitetura em camadas:
  - Routes (Flask)
  - Services (lógica de negócio)
  - Models (dados)

- Cada módulo deve ter uma única responsabilidade

---

## Estrutura de Pastas

smart-news/
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── js/
│   │   │   ├── components/
│   │   │   │   ├── auth.js
│   │   │   │   ├── newsCard.js
│   │   │   │   ├── newsFilter.js
│   │   │   │   ├── preferences.js
│   │   │   │   └── favorites.js
│   │   │   ├── pages/
│   │   │   │   ├── home.js
│   │   │   │   ├── category.js
│   │   │   │   ├── favorites.js
│   │   │   │   └── profile.js
│   │   │   ├── services/
│   │   │   │   ├── api.js
│   │   │   │   ├── authService.js
│   │   │   │   └── storageService.js
│   │   │   ├── utils/
│   │   │   │   ├── helpers.js
│   │   │   │   ├── validators.js
│   │   │   │   └── constants.js
│   │   │   └── app.js
│   │   ├── css/
│   │   │   ├── base.css
│   │   │   ├── components.css
│   │   │   ├── layout.css
│   │   │   └── responsive.css
│   │   └── assets/
│   │       └── images/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth_routes.py
│   │   │   ├── news_routes.py
│   │   │   ├── user_routes.py
│   │   │   ├── preference_routes.py
│   │   │   └── favorite_routes.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py
│   │   │   ├── news_api_service.py
│   │   │   ├── preference_service.py
│   │   │   ├── favorite_service.py
│   │   │   ├── summarizer_service.py
│   │   │   ├── recommender_service.py
│   │   │   ├── sentiment_service.py
│   │   │   └── classifier_service.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── news.py
│   │   │   ├── preference.py
│   │   │   └── favorite.py
│   │   ├── middleware/
│   │   │   ├── __init__.py
│   │   │   └── auth_middleware.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── helpers.py
│   │   │   ├── error_handler.py
│   │   │   ├── validators.py
│   │   │   └── decorators.py
│   │   └── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── schema.sql
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   ├── DATABASE.md
│   └── SETUP.md
│
├── README.md
├── CONTEXT.md
├── GUARDRAIL.md
└── .gitignore

---

## Regras Técnicas Obrigatórias
- O sistema deve utilizar sessões para autenticação
- O sistema deve utilizar bcrypt para hash de palavras-passe
- Todas as respostas do backend devem estar no formato JSON
- O sistema deve tratar erros de forma consistente

---

## Integração com API
- O sistema deve consumir API de notícias via HTTP
- O sistema deve tratar:
  - erros de rede
  - limite de requisições
  - respostas inválidas

---

## Instruções para a IA
- Explicar sempre as decisões arquiteturais e escolhas técnicas
- Fazer perguntas de esclarecimento se os requisitos forem ambíguos
- Começar com a solução mais simples que funcione
- Gerar código de forma incremental (passo a passo)

A IA não deve:
- Adicionar funcionalidades não solicitadas
- Alterar requisitos definidos

---

## Regras de Segurança
- Nunca armazenar palavras-passe em texto simples
- Validar todas as entradas do utilizador
- Evitar exposição de dados sensíveis

---

## UI/UX
- Design responsivo (mobile-first)
- Layout baseado em cards
- Interface limpa, moderna e intuitiva