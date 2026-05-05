# Projeto: Smart News

# Descrição: 

O consumo de notícias tornou-se uma atividade diária para milhões de pessoas, mas a dispersão das fontes e o volume excessivo de informação dificultam o acesso a conteúdos relevantes. Agregadores de notícias como Google News, Feedly e Inoreader resolvem este problema centralizando artigos de múltiplas fontes, organizando-os por categorias e permitindo que cada utilizador personalize a sua experiência.

# Objetivo geral: Desenvolver uma aplicação funcional e completa que: 

- Consuma notícias em tempo real a partir de uma API pública gratuita de notícias
- Permita a autenticação segura de utilizadores, incluindo registo, login e logout
- Organize as notícias por categorias e apresente-as em formato de cards
- Armazene preferências de leitura e fontes favoritas numa base de dados
- Implemente um sistema de personalização de conteúdo baseado nos interesses do  utilizador
- Integre uma funcionalidade inteligente, como resumo automático de notícias ou recomendação de artigos

# Requisitos Funcionais:  
(Autenticação de Utilizadores)
- O sistema deve permitir o registo de novos utilizadores com nome completo, correio eletrónico e palavra-passe.
- O sistema deve permitir o login utilizando correio eletrónico e palavra-passe.
- O sistema deve permitir o logout, terminando a sessão ativa.
- O sistema deve garantir a persistência da sessão durante a navegação.

(Consulta e Exibição de Notícias)
- O sistema deve permitir visualizar notícias atuais organizadas em cards.
- O sistema deve permitir filtrar notícias por categoria.
- O sistema deve permitir visualizar detalhes de cada notícia, incluindo título, descrição, fonte, data, imagem e link para o artigo original.
- O sistema deve permitir navegar por páginas ou carregar mais notícias através de paginação ou infinite scroll.

(Organização por Categorias)
- O sistema deve apresentar categorias de notícias como menu ou botões de filtro.
- O sistema deve permitir selecionar categorias como tecnologia, desporto, saúde, ciência, negócios e entretenimento.
- O sistema deve, ao selecionar uma categoria, solicitar à API apenas notícias dessa categoria.
 
(Gestão de Preferências e Favoritos)
- O sistema deve permitir ao utilizador autenticado selecionar e guardar categorias de interesse.
- O sistema deve permitir ao utilizador modificar as suas preferências a qualquer momento.
- O sistema deve permitir adicionar um artigo aos favoritos.
- O sistema deve permitir remover um artigo dos favoritos.
- O sistema deve permitir visualizar uma lista separada com apenas os artigos favoritos.

(Personalização de Conteúdo)
- O sistema deve apresentar na página inicial as notícias das categorias preferidas do utilizador com destaque.
- O sistema deve permitir ao utilizador visualizar notícias de outras categorias.
- O sistema deve lembrar as preferências do utilizador entre sessões.

(Funcionalidade Inteligente)
- O sistema deve incluir pelo menos uma funcionalidade inteligente.
- O sistema deve permitir implementar resumo automático de notícias a partir do conteúdo ou título e descrição.
- O sistema deve permitir implementar recomendação de artigos com base nas categorias preferidas e nos artigos favoritos do utilizador.
- O sistema deve permitir implementar análise de sentimento das notícias com base no título ou descrição.
- O sistema deve permitir implementar classificação automática de categorias quando a API não fornecer categoria.

(Consumo de API de Notícias)
- O sistema deve consumir notícias em tempo real a partir de uma API pública gratuita de notícias.
- O sistema deve enviar pedidos à API de notícias.
- O sistema deve receber os dados em formato JSON.
- O sistema deve extrair título, descrição, fonte, data de publicação, URL e imagem.
- O sistema deve tratar erros como chave inválida, limite de pedidos excedido ou falha na ligação.

(Persistência de Dados)
- O sistema deve armazenar preferências de leitura e fontes favoritas numa base de dados.
- O sistema deve armazenar dados de utilizadores, preferências e favoritos.
- O sistema deve permitir o armazenamento em base de dados SQLite.

# Requisitos Não Funcionais:

(Interface do Utilizador)
- O sistema deve apresentar uma interface limpa, moderna e intuitiva.
- O sistema deve seguir o padrão de cards típico de agregadores de notícias.

(Responsividade)
- O sistema deve ser responsivo e funcionar em computadores, tablets e telemóveis.

(Segurança)
- O sistema não deve armazenar palavras-passe em texto simples.
- O sistema deve utilizar hash de palavra-passe com bcrypt.

(Robustez e Tratamento de Erros)
- O sistema deve tratar erros esperados, incluindo API indisponível, limite de pedidos excedido e falhas de rede.

(Uso de Inteligência Artificial)
- O sistema deve permitir que o código fonte seja gerado por IA.
- O sistema deve garantir que os alunos compreendem a estrutura geral do código gerado.

(Arquitetura e Organização)
- O sistema deve possuir uma estrutura modular com separação entre frontend, backend, base de dados e utilitários.

(Tecnologias)
- O sistema deve utilizar apenas tecnologias gratuitas para frontend, backend, base de dados, APIs de notícias e ferramentas de IA.

# Regras de Negócio:

(Acesso ao Sistema)
- O sistema deve restringir funcionalidades como guardar preferências e favoritos apenas a utilizadores autenticados.
- O sistema deve permitir apenas a utilizadores autenticados guardar categorias preferidas.
- O sistema deve permitir apenas a utilizadores autenticados marcar artigos como favoritos.
- O sistema deve permitir apenas a utilizadores autenticados visualizar a lista de artigos favoritos.

(Preferências e Personalização)
- O sistema deve priorizar notícias com base nas preferências do utilizador.
- O sistema deve permitir modificar preferências a qualquer momento.
- O sistema deve persistir preferências entre sessões.

(Notícias)
- O sistema deve obter notícias a partir de uma API pública gratuita.

(Funcionalidade Inteligente)
- O sistema deve incluir pelo menos uma funcionalidade inteligente baseada em IA.

(Armazenamento)
- O sistema deve armazenar dados em base de dados SQLite.

(Fluxo do Utilizador)
- O sistema deve permitir ao utilizador registar-se, autenticar-se, visualizar notícias, filtrar por categoria, guardar favoritos, gerir preferências e terminar sessão.