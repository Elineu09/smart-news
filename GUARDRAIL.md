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
/frontend
  ├── index.html
  ├── login.html
  ├── register.html
  ├── styles.css
  └── app.js

/backend
  ├── app.py
  ├── routes/
  ├── services/
  ├── models/
  └── database/

/utils
  ├── api_client.py
  └── ai_features.py

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