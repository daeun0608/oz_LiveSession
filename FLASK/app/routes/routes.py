from flask import Blueprint, request, jsonify
from ..models import User
from .. import db
from sqlalchemy.exc import IntegrityError

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return 'Flask + MySQL 앱이 실행 중입니다.'

@main_bp.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'message': 'name과 email이 필요합니다.'}), 400

    user = User(name=data['name'], email=data['email'])
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': '등록 완료'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': '중복된 사용자명 또는 이메일입니다.'}), 409

@main_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'id': u.id, 'name': u.name, 'email': u.email} for u in users]
    return jsonify(result)

@main_bp.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': '사용자 없음'}), 404
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': '수정 완료'})

@main_bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': '사용자 없음'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': '삭제 완료'})

@main_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': '사용자 없음'}), 404
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    })