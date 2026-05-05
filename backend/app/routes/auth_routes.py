"""
Rotas de autenticação - Endpoints para registo, login e logout
"""
from flask import Blueprint, request, session, jsonify
from app.services.user_service import UserService
import sqlite3

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Registra um novo utilizador
    
    Body:
    {
        "nome": "string",
        "email": "string",
        "password": "string"
    }
    
    Returns:
    {
        "success": true,
        "user": {
            "id": int,
            "nome": "string",
            "email": "string"
        }
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'Dados não fornecidos'
            }), 400
        
        nome = data.get('nome', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        
        # Registar utilizador
        user = UserService.register(nome, email, password)
        
        return jsonify({
            'success': True,
            'user': user
        }), 201
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    
    except sqlite3.IntegrityError:
        return jsonify({
            'success': False,
            'error': 'Email já registado'
        }), 409
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Erro ao registar utilizador'
        }), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Autentica um utilizador e cria uma sessão
    
    Body:
    {
        "email": "string",
        "password": "string"
    }
    
    Returns:
    {
        "success": true,
        "user": {
            "id": int,
            "nome": "string",
            "email": "string"
        }
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'Dados não fornecidos'
            }), 400
        
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        
        # Validar credenciais
        user = UserService.login(email, password)
        
        # Criar sessão
        session['user_id'] = user['id']
        session['email'] = user['email']
        session.permanent = True
        
        return jsonify({
            'success': True,
            'user': user
        }), 200
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 401
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Erro ao fazer login'
        }), 500


@auth_bp.route('/logout', methods=['POST'])
def logout():
    """
    Termina a sessão do utilizador
    
    Returns:
    {
        "success": true,
        "message": "Logout realizado com sucesso"
    }
    """
    try:
        session.clear()
        return jsonify({
            'success': True,
            'message': 'Logout realizado com sucesso'
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Erro ao fazer logout'
        }), 500
