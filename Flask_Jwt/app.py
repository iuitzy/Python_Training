from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user
import datetime

app = Flask(__name__)

# Secure Key Configurations
app.config["SECRET_KEY"] = "supersecurekey123"
app.config["JWT_SECRET_KEY"] = "supersecretkey"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False  # Set True in production (HTTPS)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Dummy User Database
users = {"alice": bcrypt.generate_password_hash("password123").decode('utf-8')}

# User Class
class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(username):
    return User(username) if username in users else None

# Route: Show Login Page
@app.route('/')
def home():
    return render_template('login.html')

# Route: Authenticate User & Set JWT Cookie
@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and bcrypt.check_password_hash(users[username], password):
        access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(hours=1))

        response = make_response(redirect(url_for('dashboard')))
        response.set_cookie("access_token_cookie", access_token, httponly=True, samesite="Lax")
        login_user(User(username))

        return response
    else:
        return "Invalid credentials", 401

# Protected Route: Dashboard (Requires JWT)
@app.route('/dashboard')
@jwt_required(locations=["cookies"])
def dashboard():
    current_user = get_jwt_identity()
    return render_template('dashboard.html', username=current_user)

# Route: Logout (Clears JWT Cookie)
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('home')))
    response.set_cookie("access_token_cookie", "", expires=0)
    logout_user()
    return response

if __name__ == '__main__':
    app.run(debug=True)
