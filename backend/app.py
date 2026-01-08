import os
from flask import Flask, render_template, redirect, request, Response, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    UserMixin
)

# -------------------------------------------------
# PATH CONFIGURATION
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

app.secret_key = "supersecretkey"

# Ensure instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# -------------------------------------------------
# DATABASE CONFIG
# -------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.instance_path, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -------------------------------------------------
# LOGIN MANAGER
# -------------------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# -------------------------------------------------
# USER MODEL
# -------------------------------------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # ⚠️ plain text

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -------------------------------------------------
# LOGIN
# -------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("All fields are required", "error")
            return redirect("/")

        user = User.query.filter_by(username=username).first()

        # ⚠️ Plain text password comparison
        if user and user.password == password:
            login_user(user)
            return redirect("/dashboard")

        flash("Invalid username or password", "error")
        return redirect("/")

    return render_template("login.html")

# -------------------------------------------------
# SIGNUP
# -------------------------------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        phone = request.form.get("phone")
        password = request.form.get("password")

        if not username or not phone or not password:
            flash("All fields are required", "error")
            return redirect("/signup")

        # Phone validation (10 digits)
        if not phone.isdigit() or len(phone) != 10:
            flash("Phone number must be exactly 10 digits", "error")
            return redirect("/signup")

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
            return redirect("/signup")

        if User.query.filter_by(phone=phone).first():
            flash("Phone number already exists", "error")
            return redirect("/signup")

        # ⚠️ Store password as plain text
        user = User(
            username=username,
            phone=phone,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully. Please login.", "success")
        return redirect("/")

    return render_template("signup.html")

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

# -------------------------------------------------
# LOGOUT
# -------------------------------------------------
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# -------------------------------------------------
# YOLO VIDEO STREAM
# -------------------------------------------------
from yolo_camera import generate_frames

@app.route("/video_feed")
@login_required
def video_feed():
    return Response(
        generate_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )

# -------------------------------------------------
# RUN APPLICATION
# -------------------------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)