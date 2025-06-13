from flask import Blueprint, request
from ..models import User
from . import db

sqlite_bq = Blueprint('sqlite', __name__)

@sqlite_bq.route('/add')
def add_user():
    name=request.args.get('name')
    email=request.args.get('email')
    if name and email:
        new_user=User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return '사용자 추가 완료'

@sqlite_bq.route('/users')
def get_users():
    users=User.query.all()
    result=''   # 내용이 없을 수 있으니까 미리 생성
    for user in users:
        result+=f'{user.name} {user.email}'
    return result

@sqlite_bq.route('/update/<int:id>')
def update_user():
    user=User.query.get(id)
    if user:
        user.email='update@email.net'
        db.session.commit()
        return '사용자 이름 수정 완료'
    return '입력한 id의 데이터가 없다'

@sqlite_bq.route('/delete/<int:id>')
def delete_user(id):
    user=User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return '사용자 삭제 완료'
    return '입력한 id의 데이터가 없다'