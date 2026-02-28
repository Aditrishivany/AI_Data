import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, init_db, get_db_connection

@pytest.fixture
def client():
    """Create test client."""
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_home_redirect(client):
    """Test home page redirects to login."""
    response = client.get('/')
    assert response.status_code == 302

def test_login_page_loads(client):
    """Test login page loads successfully."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_register_page_loads(client):
    """Test register page loads successfully."""
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Register' in response.data

def test_user_registration(client):
    """Test user registration."""
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Login' in response.data

def test_registration_password_mismatch(client):
    """Test registration with mismatched passwords."""
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'different'
    })
    
    assert b'Passwords do not match' in response.data

def test_registration_short_password(client):
    """Test registration with short password."""
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': '123',
        'confirm_password': '123'
    })
    
    assert b'Password must be at least 6 characters' in response.data

def test_login(client):
    """Test user login."""
    # Register first
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    })
    
    # Then login
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_login_invalid_credentials(client):
    """Test login with invalid credentials."""
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    
    assert b'Invalid username or password' in response.data

def test_404_page(client):
    """Test 404 error page."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404' in response.data
