# Flask Login & Register Application with Docker & CI/CD

A complete Flask application with user authentication (login and register) features, fully containerized with Docker and automated CI/CD pipeline using GitHub Actions.

## Features

- **User Authentication**
  - User registration with validation
  - Secure login with password hashing
  - Session management
  - Password confirmation
  - Email validation

- **User Dashboard**
  - Welcome page after login
  - User profile view
  - Logout functionality

- **Security Features**
  - Password hashing using werkzeug.security
  - SQLite database for user storage
  - Session-based authentication
  - Input validation

- **Docker & Containerization**
  - Dockerfile for containerized deployment
  - Docker Compose for easy local development
  - Multi-stage build optimization

- **CI/CD Pipeline**
  - GitHub Actions for automated testing
  - Automated Docker image building
  - Code linting with flake8
  - Container testing on every push

## Project Structure

```
docker_pro/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose configuration
├── README.md                   # This file
├── .gitignore                  # Git ignore file
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline
└── templates/
    ├── base.html              # Base template with navigation
    ├── login.html             # Login page
    ├── register.html          # Registration page
    ├── dashboard.html         # User dashboard
    ├── profile.html           # User profile page
    ├── 404.html              # 404 error page
    └── 500.html              # 500 error page
```

## Local Development Setup

### Prerequisites
- Python 3.11+
- Docker & Docker Compose (optional)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd docker_pro
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   
   The application will be available at `http://localhost:5000`

## Docker Deployment

### Using Docker Compose (Recommended)

1. **Start the application**
   ```bash
   docker-compose up -d
   ```

2. **Access the application**
   ```
   http://localhost:5000
   ```

3. **Stop the application**
   ```bash
   docker-compose down
   ```

### Using Docker directly

1. **Build the image**
   ```bash
   docker build -t flask-auth-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 --env SECRET_KEY=your-secret-key flask-auth-app
   ```

## Testing the Application

### Register a new user
1. Navigate to `http://localhost:5000/register`
2. Fill in the registration form with:
   - Username (minimum 3 characters)
   - Email (valid email format)
   - Password (minimum 6 characters)
   - Confirm Password
3. Click Register

### Login
1. Navigate to `http://localhost:5000/login`
2. Enter your username and password
3. Click Login

### Access Dashboard
- After login, you'll be redirected to the dashboard
- Click "Profile" to view your account information
- Click "Logout" to logout

## CI/CD Pipeline

The GitHub Actions workflow runs on every push and pull request:

1. **Code Quality**
   - Lints code with flake8
   - Checks for syntax errors

2. **Build & Test**
   - Builds Docker image
   - Tests Docker container startup
   - Verifies application responds

3. **Deployment** (on main branch push only)
   - Builds production Docker image
   - Ready for deployment to cloud platforms

### GitHub Actions Workflow
See `.github/workflows/ci-cd.yml` for the complete pipeline configuration.

## Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```

## Database

- **Type**: SQLite3
- **File**: `users.db` (created automatically)
- **Schema**: Single `users` table with id, username, email, password, and created_at

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page (redirects to login) |
| `/register` | GET, POST | User registration |
| `/login` | GET, POST | User login |
| `/dashboard` | GET | User dashboard |
| `/profile` | GET | User profile |
| `/logout` | GET | User logout |

## Security Best Practices Implemented

- ✅ Password hashing with werkzeug.security
- ✅ Session-based authentication
- ✅ Input validation
- ✅ Protected routes (require login)
- ✅ CSRF protection ready (add Flask-WTF for forms)
- ✅ Environment-based configuration

## Future Enhancements

- [ ] Email verification on registration
- [ ] Password reset functionality
- [ ] Two-factor authentication
- [ ] OAuth integration (Google, GitHub)
- [ ] User profile updates
- [ ] Rate limiting on login attempts
- [ ] Database migrations with Alembic
- [ ] Unit tests with pytest

## Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue in the repository.

---

**Happy Coding! 🚀**
