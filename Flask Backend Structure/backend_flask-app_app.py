from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from datetime import datetime
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes
from routes.auth import auth_bp
from routes.profiles import profiles_bp
from routes.matches import matches_bp

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(profiles_bp)
app.register_blueprint(matches_bp)

# Sample data (in production, use database)
users = [
    {
        'id': 1,
        'name': 'Happiness Manana',
        'age': 23,
        'location': 'Johannesburg, SA',
        'interests': ['Travel', 'Music', 'Food'],
        'bio': 'Adventurous soul looking for someone to explore the world with.',
        'image': 'profile1.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()})

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])
