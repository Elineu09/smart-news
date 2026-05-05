"""
Modelo de utilizador - Camada de dados para manipulação de utilizadores
"""
from database.db import get_db


class User:
    """Representa um utilizador na aplicação"""
    
    def __init__(self, id=None, nome=None, email=None, password_hash=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.password_hash = password_hash
    
    @staticmethod
    def create(nome, email, password_hash):
        """
        Cria um novo utilizador na base de dados
        
        Args:
            nome: Nome completo do utilizador
            email: Email único do utilizador
            password_hash: Hash da palavra-passe (já processado com bcrypt)
        
        Returns:
            User: Objeto User com o id gerado
        
        Raises:
            sqlite3.IntegrityError: Se o email já existe
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (nome, email, password_hash)
                VALUES (?, ?, ?)
            ''', (nome, email, password_hash))
            
            user_id = cursor.lastrowid
            return User(id=user_id, nome=nome, email=email, password_hash=password_hash)
    
    @staticmethod
    def find_by_email(email):
        """
        Encontra um utilizador pelo email
        
        Args:
            email: Email do utilizador
        
        Returns:
            User: Objeto User se encontrado, None caso contrário
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nome, email, password_hash FROM users WHERE email = ?', (email,))
            row = cursor.fetchone()
            
            if row:
                return User(
                    id=row['id'],
                    nome=row['nome'],
                    email=row['email'],
                    password_hash=row['password_hash']
                )
            return None
    
    @staticmethod
    def find_by_id(user_id):
        """
        Encontra um utilizador pelo id
        
        Args:
            user_id: ID do utilizador
        
        Returns:
            User: Objeto User se encontrado, None caso contrário
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nome, email, password_hash FROM users WHERE id = ?', (user_id,))
            row = cursor.fetchone()
            
            if row:
                return User(
                    id=row['id'],
                    nome=row['nome'],
                    email=row['email'],
                    password_hash=row['password_hash']
                )
            return None
    
    def to_dict(self):
        """
        Converte o objeto User para dicionário (sem a password_hash)
        
        Returns:
            dict: Dicionário com dados do utilizador
        """
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
