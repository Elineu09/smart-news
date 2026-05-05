"""
Módulo de serviços da aplicação
Contém toda a lógica de negócio
"""
from .user_service import UserService

__all__ = ['UserService']

from .news_api_service import NewsAPIService

__all__ = ["NewsAPIService"]
