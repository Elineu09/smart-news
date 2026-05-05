"""
Pacote de base de dados - gerenciamento de conexões e inicialização
"""
from .db import get_db, init_db, get_connection

__all__ = ['get_db', 'init_db', 'get_connection']
