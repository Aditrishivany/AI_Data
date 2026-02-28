from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

DATABASE = 'users.db'

def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with users table."""
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

@app.before_request
def before_request():
    """Initialize database before first request."""
    if not os.path.exists(DATABASE):
        init_db()

@app.route('/')
def index():
    """Home page route."""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    error = None
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            error = 'All fields are required'
        elif len(username) < 3:
            error = 'Username must be at least 3 characters long'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters long'
        elif password != confirm_password:
            error = 'Passwords do not match'
        elif '@' not in email:
            error = 'Invalid email address'
        
        if error is None:
            try:
                conn = get_db_connection()
                conn.execute(
                    'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                    (username, email, generate_password_hash(password))
                )
                conn.commit()
                conn.close()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                error = 'Username or email already exists'
    
    return render_template('register.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    error = None
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            error = 'Username and password are required'
        else:
            conn = get_db_connection()
            user = conn.execute(
                'SELECT * FROM users WHERE username = ?',
                (username,)
            ).fetchone()
            conn.close()
            
            if user is None or not check_password_hash(user['password'], password):
                error = 'Invalid username or password'
            else:
                session.clear()
                session['user_id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('dashboard'))
    
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    """User dashboard route."""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/logout')
def logout():
    """User logout route."""
    session.clear()
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    """User profile route."""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE id = ?',
        (session['user_id'],)
    ).fetchone()
    conn.close()
    
    return render_template('profile.html', user=user)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
