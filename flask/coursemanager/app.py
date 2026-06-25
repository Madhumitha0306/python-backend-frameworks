from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from courses.routes import courses_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(courses_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()