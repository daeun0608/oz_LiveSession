from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/add')
def add_user():
    name=request.args.get('name')
    email=request.args.get('email')
    if name and email:
        new_user=User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return '사용자 추가 완료'

@app.route('/users')
def get_users():
    users=User.query.all()
    result=''   # 내용이 없을 수 있으니까 미리 생성
    for user in users:
        result+=f'{user.name} {user.email}'
    return result

@app.route('/update/<int:id>')
def update_user():
    user=User.query.get(id)
    if user:
        user.email='update@email.net'
        db.session.commit()
        return '사용자 이름 수정 완료'
    return '입력한 id의 데이터가 없다'

@app.route('/delete/<int:id>')
def delete_user(id):
    user=User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return '사용자 삭제 완료'
    return '입력한 id의 데이터가 없다'
    
@app.route('/')
def index():  # put application's code here
    return 'Flask DB 완료'

# @app.route('/shop')     # get 예시
# def shop():
#     keyword=request.args.get('keyword')
#     category=request.args.get('category')
#     return f'검색어 : {keyword}, 카테고리 : {category}'
#
# @app.route('/filter')       # getlist 예시
# def filter():
#     filter=request.args.getlist('filter')
#     return f'적용한 필터 : {filter}'
#
# @app.route('/greet/<username>/<int:age>')     # < >안에 데이터 타입을 정할 수 있음, 기본 string(int, float, path-/가 포함되는 문자열)
# def greet_user(username, age):
#     return f'안녕, {username}! 나는 {age}살이야 우리 친구하자.'
#
# @app.route('/calc/<int:a>/<operator>/<int:b>')      # 계산기
# def calc(a,operator,b):
#     try:
#         if operator == "add":
#             return f'Result: {a+b}'
#         elif operator == "sub":
#             return f'Result: {a - b}'
#         elif operator == "mul":
#             return f'Result: {a * b}'
#         elif operator == "div":
#             return f'Result: {a / b}'
#         else :
#             return 'add, sub, mul, div 중에 하나를 다시 입력해주세요'
#     except ZeroDivisionError:
#         return 'error : ZeroDivisionError'
#
# @app.route('/birthyear/<int:age>')      # 타입힌팅
# def birthyear(age : int)-> str:
#     return f'당신은 {2025-age}에 태어났다!'
#
# @app.route('/user')     # jsonify 이용
# def get_user():
#     user = {"name":"지수", "age":24}
#     return jsonify(user), 400       # 상태코드 ( 화면이 아닌 개발자 창의 네트워크에서 확인이 가능하다 )
#
# @app.route('/custom-header')    # 헤더에 정보 추가 ( 네트워크에서 헤더 정보 확인 )
# def custom_header():
#     response=jsonify({"message":"헤더가 포함된 응답입니다."})
#     response.headers['oz-good']='1.0.0'
#     return response
#
# @app.route('/name/<name>')      # 변수넣기
# def show_name(name : str) ->str :
#     return render_template("index.html",index_name=name)

if __name__ == '__main__':
    app.run(debug=True)
