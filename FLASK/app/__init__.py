from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
# db=SQLAlchemy(app)
# with app.app_context():
#     db.create_all()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0070@localhost:3306/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .models import User
    with app.app_context():
        db.create_all()  # 테이블 생성

    from app.routes.routes import main_bp
    from app.routes.user import user_bq
    from app.routes.basic import basic_bq   
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bq)
    app.register_blueprint(basic_bq)
    return app


