"""
Middleware de autenticação - Decoradores e funções auxiliares
"""
from flask import session, jsonify
from functools import wraps
from app.services.user_service import UserService


def login_required(f):
    """
    Decorador para rotas que requerem autenticação
    
    Verifica se user_id está na sessão
    Se não, retorna erro 401
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({
                'success': False,
                'error': 'Autenticação necessária'
            }), 401
        
        return f(*args, **kwargs)
    
    return decorated_function


def get_current_user():
    """
    Obtém o utilizador atual da sessão
    
    Returns:
        dict: Dados do utilizador ou None se não autenticado
    """
    if 'user_id' not in session:
        return None
    
    return UserService.get_user_by_id(session['user_id'])
