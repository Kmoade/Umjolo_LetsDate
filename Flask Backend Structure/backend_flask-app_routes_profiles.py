from flask import Blueprint, render_template, session, redirect, url_for, jsonify

profiles_bp = Blueprint('profiles', __name__)

# Sample data
users = [
    {
        'id': 1,
        'name': 'Happiness Manana',
        'age': 23,
        'location': 'Johannesburg, SA',
        'interests': ['Travel', 'Music', 'Food'],
        'bio': 'Adventurous soul looking for someone to explore the world with.',
        'image': 'https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
    }
]

@profiles_bp.route('/profiles')
def profiles_page():
    if not session.get('user'):
        return redirect(url_for('auth.login'))
    return render_template('profiles.html', users=users)

@profiles_bp.route('/api/profiles')
def api_profiles():
    return jsonify(users)
