"""
Aplicação Flask - Configuração principal
"""
from flask import Flask
from flask_session import Session
import os
from datetime import timedelta
from database import init_db
from app.routes.auth_routes import auth_bp


def create_app():
    """
    Factory function para criar e configurar a aplicação Flask
    
    Returns:
        Flask: Aplicação Flask configurada
    """
    app = Flask(__name__)
    
    # Configuração
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    
    # Inicializar sessões
    Session(app)
    
    # Inicializar base de dados
    with app.app_context():
        init_db()
    
    # Registar blueprints
    app.register_blueprint(auth_bp)
    
    # Health check
    @app.route('/api/health', methods=['GET'])
    def health():
        return {'status': 'ok'}, 200
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
