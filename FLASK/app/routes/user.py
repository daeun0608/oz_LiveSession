from flask import Blueprint, render_template

user_bq = Blueprint('user', __name__)

@user_bq.route('/name/<name>')      # 변수넣기
def show_name(name : str) ->str :
    return render_template("index.html",index_name=name)