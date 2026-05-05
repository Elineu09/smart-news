"""
Testes das rotas de autenticação
"""
import unittest
import json
import sys
import os

# Adicionar o diretório backend ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import create_app
from database import init_db


class AuthRoutesTestCase(unittest.TestCase):
    """Testes para as rotas de autenticação"""
    
    def setUp(self):
        """Configuração antes de cada teste"""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SESSION_TYPE'] = 'filesystem'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            init_db()
    
    def test_register_success(self):
        """Testa registo bem-sucedido"""
        response = self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'João Silva',
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['user']['nome'], 'João Silva')
        self.assertEqual(data['user']['email'], 'joao@example.com')
    
    def test_register_duplicate_email(self):
        """Testa registo com email duplicado"""
        # Primeiro registo
        self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'João Silva',
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        # Segundo registo com mesmo email
        response = self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'Maria Silva',
                'email': 'joao@example.com',
                'password': 'password456'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 409)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_register_short_password(self):
        """Testa registo com password curta"""
        response = self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'João Silva',
                'email': 'joao@example.com',
                'password': '123'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_login_success(self):
        """Testa login bem-sucedido"""
        # Registar primeiro
        self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'João Silva',
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        # Login
        response = self.client.post(
            '/api/auth/login',
            data=json.dumps({
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['user']['email'], 'joao@example.com')
    
    def test_login_wrong_password(self):
        """Testa login com password errada"""
        # Registar primeiro
        self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'João Silva',
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        # Login com password errada
        response = self.client.post(
            '/api/auth/login',
            data=json.dumps({
                'email': 'joao@example.com',
                'password': 'wrongpassword'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_login_user_not_found(self):
        """Testa login com email inexistente"""
        response = self.client.post(
            '/api/auth/login',
            data=json.dumps({
                'email': 'inexistente@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 401)
        data = json.loads(response.data)
        self.assertFalse(data['success'])
    
    def test_logout(self):
        """Testa logout"""
        # Registar e fazer login
        self.client.post(
            '/api/auth/register',
            data=json.dumps({
                'nome': 'João Silva',
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        self.client.post(
            '/api/auth/login',
            data=json.dumps({
                'email': 'joao@example.com',
                'password': 'password123'
            }),
            content_type='application/json'
        )
        
        # Logout
        response = self.client.post('/api/auth/logout')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])


if __name__ == '__main__':
    unittest.main()
