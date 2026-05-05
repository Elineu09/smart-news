"""
Módulo responsável pelo consumo da API NewsAPI.org.

Endpoints:
- https://newsapi.org/v2/top-headlines

Tratamento de erros:
- Chave de API inválida (401)
- Limite de requisições excedido (429)
- Falha de conexão
"""

import requests
from typing import List, Dict, Optional


class NewsAPIService:
    """Serviço para consumir notícias da API NewsAPI.org."""

    BASE_URL = "https://newsapi.org/v2"
    TIMEOUT = 10

    def __init__(self, api_key: str):
        """
        Inicializa o serviço.

        Args:
            api_key: Chave de autenticação da API NewsAPI
        """
        if not api_key or not api_key.strip():
            raise ValueError("Chave de API não pode estar vazia")

        self.api_key = api_key

    def _make_request(self, endpoint: str, params: Dict) -> Dict:
        """
        Realiza uma requisição HTTP à API.

        Args:
            endpoint: Endpoint da API (ex: "top-headlines")
            params: Parâmetros da requisição

        Returns:
            Resposta JSON da API

        Raises:
            Exception: Em caso de erro na requisição
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {"X-Api-Key": self.api_key}

        try:
            response = requests.get(url, params=params, headers=headers, timeout=self.TIMEOUT)

            if response.status_code == 401:
                raise Exception("Erro: Chave de API inválida ou expirada")

            if response.status_code == 429:
                raise Exception("Erro: Limite de requisições excedido. Tente novamente mais tarde")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            raise Exception("Erro: Timeout na conexão com a API")

        except requests.exceptions.ConnectionError:
            raise Exception("Erro: Falha de conexão com a API")

        except requests.exceptions.HTTPError as e:
            raise Exception(f"Erro HTTP {response.status_code}: {str(e)}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {str(e)}")

    def _extract_article_fields(self, article: Dict) -> Optional[Dict]:
        """
        Extrai apenas os campos necessários de um artigo.

        Args:
            article: Dicionário com dados do artigo da API

        Returns:
            Dicionário com campos padronizados ou None se falhar
        """
        try:
            return {
                "title": article.get("title", ""),
                "description": article.get("description", ""),
                "source": article.get("source", {}).get("name", ""),
                "published_at": article.get("publishedAt", ""),
                "url": article.get("url", ""),
                "image": article.get("urlToImage", "")
            }
        except (KeyError, AttributeError, TypeError):
            return None

    def get_top_headlines(self, category: Optional[str] = None, 
                         country: str = "us", page_size: int = 20) -> List[Dict]:
        """
        Obtém as principais notícias.

        Args:
            category: Categoria de notícias (opcional)
            country: Código do país (padrão: "us")
            page_size: Número de notícias a retornar (máximo 100)

        Returns:
            Lista de dicionários com artigos padronizados

        Raises:
            Exception: Se houver erro na requisição
        """
        params = {"pageSize": min(page_size, 100)}

        if category:
            params["category"] = category
        else:
            params["country"] = country

        response = self._make_request("top-headlines", params)

        if response.get("status") != "ok":
            error_msg = response.get("message", "Erro desconhecido na API")
            raise Exception(f"Erro na API: {error_msg}")

        articles = response.get("articles", [])
        processed_articles = []

        for article in articles:
            processed = self._extract_article_fields(article)
            if processed:
                processed_articles.append(processed)

        return processed_articles
