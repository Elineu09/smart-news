"""
Serviço de utilizadores - Lógica de negócio para autenticação
"""
import bcrypt
import sqlite3
from app.models.user import User


class UserService:
    """Serviço para gerenciar operações de utilizadores"""
    
    @staticmethod
    def register(nome, email, password):
        """
        Registra um novo utilizador
        
        Args:
            nome: Nome completo do utilizador
            email: Email único do utilizador
            password: Palavra-passe em texto simples
        
        Returns:
            dict: Dados do utilizador registado (sem password_hash)
        
        Raises:
            ValueError: Se email já existe ou dados inválidos
            sqlite3.IntegrityError: Se email já existe na base de dados
        """
        # Validações
        if not nome or not email or not password:
            raise ValueError("Nome, email e palavra-passe são obrigatórios")
        
        if len(password) < 6:
            raise ValueError("Palavra-passe deve ter pelo menos 6 caracteres")
        
        if '@' not in email:
            raise ValueError("Email inválido")
        
        # Verificar se email já existe
        if User.find_by_email(email):
            raise ValueError("Email já registado")
        
        # Hash da palavra-passe
        password_hash = UserService._hash_password(password)
        
        try:
            user = User.create(nome, email, password_hash)
            return user.to_dict()
        except sqlite3.IntegrityError:
            raise ValueError("Email já registado")
    
    @staticmethod
    def login(email, password):
        """
        Verifica credenciais de login
        
        Args:
            email: Email do utilizador
            password: Palavra-passe em texto simples
        
        Returns:
            dict: Dados do utilizador se credenciais válidas
        
        Raises:
            ValueError: Se credenciais inválidas
        """
        if not email or not password:
            raise ValueError("Email e palavra-passe são obrigatórios")
        
        user = User.find_by_email(email)
        
        if not user:
            raise ValueError("Email ou palavra-passe incorretos")
        
        # Verificar password
        if not UserService._verify_password(password, user.password_hash):
            raise ValueError("Email ou palavra-passe incorretos")
        
        return user.to_dict()
    
    @staticmethod
    def get_user_by_id(user_id):
        """
        Obtém dados de um utilizador pelo id
        
        Args:
            user_id: ID do utilizador
        
        Returns:
            dict: Dados do utilizador ou None se não encontrado
        """
        user = User.find_by_id(user_id)
        return user.to_dict() if user else None
    
    @staticmethod
    def _hash_password(password):
        """
        Gera hash bcrypt de uma palavra-passe
        
        Args:
            password: Palavra-passe em texto simples
        
        Returns:
            str: Hash bcrypt da palavra-passe
        """
        salt = bcrypt.gensalt(rounds=10)
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    @staticmethod
    def _verify_password(password, password_hash):
        """
        Verifica se uma palavra-passe corresponde ao seu hash
        
        Args:
            password: Palavra-passe em texto simples
            password_hash: Hash bcrypt armazenado
        
        Returns:
            bool: True se a palavra-passe está correta
        """
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
