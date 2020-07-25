from flask_sqlalchemy import SQLAlchemy

# Objeto criado apenas uma vez e usado em todo o programa (singleton)

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)