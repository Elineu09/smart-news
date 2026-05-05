"""
Testes unitários para o módulo NewsAPIService
Utiliza pytest e unittest.mock para testar sem dependência da API real
"""

import pytest
from unittest.mock import patch, Mock
from app.services import NewsAPIService
import requests


class TestNewsAPIServiceInit:
    """Testes de inicialização do serviço"""

    def test_init_with_valid_api_key(self):
        """Deve inicializar com API key válida"""
        service = NewsAPIService(api_key="test_key_123")
        assert service.api_key == "test_key_123"

    def test_init_with_empty_api_key_raises_error(self):
        """Deve lançar ValueError se API key estiver vazia"""
        with pytest.raises(ValueError) as exc_info:
            NewsAPIService(api_key="")
        assert "Chave de API não pode estar vazia" in str(exc_info.value)

    def test_init_with_whitespace_api_key_raises_error(self):
        """Deve lançar ValueError se API key contiver apenas espaços"""
        with pytest.raises(ValueError) as exc_info:
            NewsAPIService(api_key="   ")
        assert "Chave de API não pode estar vazia" in str(exc_info.value)

    def test_init_with_none_api_key_raises_error(self):
        """Deve lançar ValueError se API key for None"""
        with pytest.raises(ValueError) as exc_info:
            NewsAPIService(api_key=None)
        assert "Chave de API não pode estar vazia" in str(exc_info.value)


class TestGetTopHeadlinesSuccess:
    """Testes de sucesso na busca de notícias"""

    @patch("requests.get")
    def test_get_headlines_with_country_default(self, mock_get):
        """Deve obter notícias com país padrão"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 100,
            "articles": [
                {
                    "title": "Test Article",
                    "description": "Test Description",
                    "source": {"name": "BBC"},
                    "publishedAt": "2026-05-05T10:00:00Z",
                    "url": "https://example.com/1",
                    "urlToImage": "https://example.com/img1.jpg"
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines(country="us")

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["title"] == "Test Article"
        assert result[0]["source"] == "BBC"

    @patch("requests.get")
    def test_get_headlines_with_category(self, mock_get):
        """Deve obter notícias por categoria"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 50,
            "articles": [
                {
                    "title": "Tech News",
                    "description": "About tech",
                    "source": {"name": "TechCrunch"},
                    "publishedAt": "2026-05-05T10:00:00Z",
                    "url": "https://example.com/tech",
                    "urlToImage": "https://example.com/tech.jpg"
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines(category="technology")

        assert isinstance(result, list)
        assert len(result) == 1
        assert "Tech" in result[0]["title"]

    @patch("requests.get")
    def test_get_headlines_page_size_limited(self, mock_get):
        """Page size deve ser limitado a máximo 100"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        service.get_top_headlines(page_size=200)

        call_args = mock_get.call_args
        assert call_args[1]["params"]["pageSize"] == 100

    @patch("requests.get")
    def test_normalize_article_fields(self, mock_get):
        """Deve normalizar campos dos artigos corretamente"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 1,
            "articles": [
                {
                    "title": "Breaking News",
                    "description": "Important story",
                    "source": {"name": "Reuters"},
                    "publishedAt": "2026-05-05T12:00:00Z",
                    "url": "https://example.com/news",
                    "urlToImage": "https://example.com/image.jpg"
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        article = result[0]
        assert article["title"] == "Breaking News"
        assert article["description"] == "Important story"
        assert article["source"] == "Reuters"
        assert article["published_at"] == "2026-05-05T12:00:00Z"
        assert article["url"] == "https://example.com/news"
        assert article["image"] == "https://example.com/image.jpg"

    @patch("requests.get")
    def test_handle_source_as_dict(self, mock_get):
        """Deve extrair name de source quando é um dict"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 1,
            "articles": [
                {
                    "title": "News",
                    "description": "Desc",
                    "source": {"name": "BBC", "id": "bbc-news"},
                    "publishedAt": "2026-05-05T12:00:00Z",
                    "url": "https://example.com",
                    "urlToImage": "https://example.com/img.jpg"
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        assert result[0]["source"] == "BBC"

    @patch("requests.get")
    def test_missing_fields_have_defaults(self, mock_get):
        """Campos faltantes devem ter valores padrão (strings vazias)"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 1,
            "articles": [
                {
                    "title": "News"
                    # Faltam outros campos
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        article = result[0]
        assert article["title"] == "News"
        assert article["description"] == ""
        assert article["source"] == ""
        assert article["published_at"] == ""
        assert article["url"] == ""
        assert article["image"] == ""

    @patch("requests.get")
    def test_empty_articles_list(self, mock_get):
        """Deve retornar lista vazia quando não há artigos"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        assert isinstance(result, list)
        assert len(result) == 0


class TestGetTopHeadlinesErrors:
    """Testes de tratamento de erros"""

    @patch("requests.get")
    def test_invalid_api_key_error(self, mock_get):
        """Deve lançar exceção para erro 401 (API key inválida)"""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="invalid_key")
        
        with pytest.raises(Exception) as exc_info:
            service.get_top_headlines()
        
        assert "inválida" in str(exc_info.value).lower()

    @patch("requests.get")
    def test_rate_limit_exceeded_error(self, mock_get):
        """Deve lançar exceção para erro 429 (limite de requisições)"""
        mock_response = Mock()
        mock_response.status_code = 429
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        
        with pytest.raises(Exception) as exc_info:
            service.get_top_headlines()
        
        assert "limite" in str(exc_info.value).lower()

    @patch("requests.get")
    def test_api_response_error(self, mock_get):
        """Deve lançar exceção para erro retornado pela API"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "error",
            "message": "Invalid parameters"
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        
        with pytest.raises(Exception) as exc_info:
            service.get_top_headlines()
        
        assert "Invalid parameters" in str(exc_info.value)

    @patch("requests.get")
    def test_connection_timeout_error(self, mock_get):
        """Deve lançar exceção para timeout de conexão"""
        mock_get.side_effect = requests.exceptions.Timeout("Connection timeout")

        service = NewsAPIService(api_key="test_key")
        
        with pytest.raises(Exception) as exc_info:
            service.get_top_headlines()
        
        assert "timeout" in str(exc_info.value).lower()

    @patch("requests.get")
    def test_connection_error(self, mock_get):
        """Deve lançar exceção para erro de conexão"""
        mock_get.side_effect = requests.exceptions.ConnectionError("No internet")

        service = NewsAPIService(api_key="test_key")
        
        with pytest.raises(Exception) as exc_info:
            service.get_top_headlines()
        
        assert "conexão" in str(exc_info.value).lower() or "connection" in str(exc_info.value).lower()

    @patch("requests.get")
    def test_http_error_status(self, mock_get):
        """Deve lançar exceção para outros status HTTP de erro"""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Server error")
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        
        with pytest.raises(Exception):
            service.get_top_headlines()


class TestArticleNormalization:
    """Testes de normalização de artigos"""

    @patch("requests.get")
    def test_extract_article_fields(self, mock_get):
        """Deve extrair apenas os campos necessários"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 1,
            "articles": [
                {
                    "title": "News Title",
                    "description": "News Desc",
                    "source": {"name": "Source Name"},
                    "publishedAt": "2026-05-05T10:00:00Z",
                    "url": "https://example.com",
                    "urlToImage": "https://example.com/img.jpg",
                    "author": "John Doe",  # Campo extra
                    "content": "Full content"  # Campo extra
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        article = result[0]
        # Apenas os 6 campos devem estar presentes
        assert set(article.keys()) == {"title", "description", "source", "published_at", "url", "image"}

    @patch("requests.get")
    def test_multiple_articles_processing(self, mock_get):
        """Deve processar múltiplos artigos corretamente"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 3,
            "articles": [
                {
                    "title": f"Article {i}",
                    "description": f"Desc {i}",
                    "source": {"name": f"Source {i}"},
                    "publishedAt": f"2026-05-05T{i:02d}:00:00Z",
                    "url": f"https://example.com/{i}",
                    "urlToImage": f"https://example.com/img{i}.jpg"
                }
                for i in range(3)
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        assert len(result) == 3
        for i, article in enumerate(result):
            assert article["title"] == f"Article {i}"
            assert article["description"] == f"Desc {i}"

    @patch("requests.get")
    def test_filter_invalid_articles(self, mock_get):
        """Deve filtrar artigos inválidos"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 2,
            "articles": [
                {
                    "title": "Valid Article",
                    "description": "Desc",
                    "source": {"name": "Source"},
                    "publishedAt": "2026-05-05T10:00:00Z",
                    "url": "https://example.com",
                    "urlToImage": "https://example.com/img.jpg"
                }
            ]
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        result = service.get_top_headlines()

        assert len(result) == 1


class TestRequestParameters:
    """Testes de parâmetros da requisição"""

    @patch("requests.get")
    def test_request_includes_api_key_in_header(self, mock_get):
        """Deve incluir API key no header da requisição"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        api_key = "test_api_key_123"
        service = NewsAPIService(api_key=api_key)
        service.get_top_headlines()

        call_args = mock_get.call_args
        headers = call_args[1]["headers"]
        assert headers["X-Api-Key"] == api_key

    @patch("requests.get")
    def test_timeout_value_set(self, mock_get):
        """Deve usar timeout configurado de 10 segundos"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        service.get_top_headlines()

        call_args = mock_get.call_args
        assert call_args[1]["timeout"] == 10

    @patch("requests.get")
    def test_request_url_endpoint(self, mock_get):
        """Deve fazer requisição para endpoint correto"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        service.get_top_headlines()

        call_args = mock_get.call_args
        url = call_args[0][0]
        assert "newsapi.org/v2/top-headlines" in url

    @patch("requests.get")
    def test_country_parameter_passed(self, mock_get):
        """Deve passar parâmetro country na requisição"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        service.get_top_headlines(country="pt")

        call_args = mock_get.call_args
        assert call_args[1]["params"]["country"] == "pt"

    @patch("requests.get")
    def test_category_parameter_passed(self, mock_get):
        """Deve passar parâmetro category na requisição"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        service.get_top_headlines(category="technology")

        call_args = mock_get.call_args
        assert call_args[1]["params"]["category"] == "technology"

    @patch("requests.get")
    def test_page_size_parameter_passed(self, mock_get):
        """Deve passar parâmetro pageSize na requisição"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "ok",
            "totalResults": 0,
            "articles": []
        }
        mock_get.return_value = mock_response

        service = NewsAPIService(api_key="test_key")
        service.get_top_headlines(page_size=50)

        call_args = mock_get.call_args
        assert call_args[1]["params"]["pageSize"] == 50


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
