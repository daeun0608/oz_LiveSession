from flask import Blueprint, request, jsonify

basic_bq = Blueprint('basic', __name__)

@basic_bq.route('/shop')     # get 예시
def shop():
    keyword=request.args.get('keyword')
    category=request.args.get('category')
    return f'검색어 : {keyword}, 카테고리 : {category}'

@basic_bq.route('/filter')       # getlist 예시
def filter():
    filter=request.args.getlist('filter')
    return f'적용한 필터 : {filter}'

@basic_bq.route('/greet/<username>/<int:age>')     # < >안에 데이터 타입을 정할 수 있음, 기본 string(int, float, path-/가 포함되는 문자열)
def greet_user(username, age):
    return f'안녕, {username}! 나는 {age}살이야 우리 친구하자.'

@basic_bq.route('/calc/<int:a>/<operator>/<int:b>')      # 계산기
def calc(a,operator,b):
    try:
        if operator == "add":
            return f'Result: {a+b}'
        elif operator == "sub":
            return f'Result: {a - b}'
        elif operator == "mul":
            return f'Result: {a * b}'
        elif operator == "div":
            return f'Result: {a / b}'
        else :
            return 'add, sub, mul, div 중에 하나를 다시 입력해주세요'
    except ZeroDivisionError:
        return 'error : ZeroDivisionError'

@basic_bq.route('/birthyear/<int:age>')      # 타입힌팅
def birthyear(age : int)-> str:
    return f'당신은 {2025-age}에 태어났다!'

@basic_bq.route('/user')     # jsonify 이용
def get_user():
    user = {"name":"지수", "age":24}
    return jsonify(user), 400       # 상태코드 ( 화면이 아닌 개발자 창의 네트워크에서 확인이 가능하다 )

@basic_bq.route('/custom-header')    # 헤더에 정보 추가 ( 네트워크에서 헤더 정보 확인 )
def custom_header():
    response=jsonify({"message":"헤더가 포함된 응답입니다."})
    response.headers['oz-good']='1.0.0'
    return response