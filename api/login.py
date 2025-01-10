import hashlib
import os
import jwt
import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuration de JWT
SECRET_KEY = 'my-secret-key'

# Configuration de Swagger
SWAGGER_URL = '/docs'  # URL pour accéder à la documentation Swagger
API_URL = '/swagger.json'  # Lien vers le fichier OpenAPI (swagger.json)
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Fonction pour générer un token JWT
def generate_token(user_id):
    expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1)  # Token valable 1h
    token = jwt.encode({
        'sub': user_id,
        'exp': expiration_time
    }, SECRET_KEY, algorithm='HS256')
    return token

# Fonction pour créer un hash avec un salt
def create_password_hash(password, salt=None):
    if not salt:
        salt = os.urandom(16).hex()
    salted_password = salt + password
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    return password_hash, salt

# Base d'utilisateurs
users = {}

default_user = "admin@example.com"
default_password = "mypassword"
default_name = "Admin User"
password_hash, salt = create_password_hash(default_password)

users[default_user] = {
    "password_hash": password_hash,
    "salt": salt,
    "name": default_name
}

# Fonction pour vérifier le mot de passe
def verify_password(stored_hash, password, salt):
    salted_password = salt + password
    computed_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    return computed_hash == stored_hash

# Retourne la documentation Swagger
@app.route('/swagger.json')
def swagger_spec():
    return send_from_directory('.', 'swagger.json')

# Route pour la connexion
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email et mot de passe requis."}), 400

        user = users.get(email)
        if user and verify_password(user['password_hash'], password, user['salt']):
            token = generate_token(email)
            return jsonify({
                "message": "Connexion réussie.",
                "user": {"email": email, "name": user['name']},
                "token": token
            }), 200
        else:
            return jsonify({"error": "Email ou mot de passe incorrect."}), 401

    except Exception as e:
        return jsonify({"error": "Une erreur est survenue.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
