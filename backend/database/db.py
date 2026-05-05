"""
Módulo de configuração e gerenciamento da base de dados SQLite
"""
import sqlite3
import os
from contextlib import contextmanager

# Caminho da base de dados
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'news.db')


def get_connection():
    """Retorna uma conexão com a base de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def get_db():
    """Context manager para gerenciar conexões com a base de dados"""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def init_db():
    """Inicializa a base de dados com as tabelas necessárias"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabela de utilizadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
