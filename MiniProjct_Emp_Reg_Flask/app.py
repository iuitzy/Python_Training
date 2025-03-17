from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
import datetime
from models import User, db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        if User.query.filter_by(username=username).first():
            return jsonify({"message": "User already exists"}), 400

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(hours=1))
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('jwt', access_token, httponly=True, secure=True)
            return response
        return jsonify({"message": "Invalid credentials"}), 401
    return render_template('login.html')

@app.route('/dashboard')
@jwt_required()
def dashboard():
    username = get_jwt_identity()
    return render_template('dashboard.html', username=username)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('home')))
    response.set_cookie('jwt', '', expires=0, httponly=True, secure=True)
    return response

if __name__ == '__main__':
    app.run(debug=True)
