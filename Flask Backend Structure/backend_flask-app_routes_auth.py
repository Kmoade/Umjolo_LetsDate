from flask import Blueprint, request, session, redirect, url_for, render_template, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email and password:
            session['user'] = {'email': email, 'logged_in': True}
            return redirect(url_for('profiles.profiles_page'))
    
    return render_template('auth.html', mode='login')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if name and email and password:
            session['user'] = {'name': name, 'email': email, 'logged_in': True}
            return redirect(url_for('profiles.profiles_page'))
    
    return render_template('auth.html', mode='signup')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))
