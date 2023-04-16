from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo
import importlib, sys
importlib.reload(sys)

app = Flask(__name__)
app.secret_key = 'itheima'

class SubmitForm(FlaskForm):
    flag = StringField('Flag：',validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/form',methods=['GET','POST'])
def submit():
    form = SubmitForm()
    # 1.判断请求方式
        # 2.获取请求的参数
        # 3.调用validation_on_submit方法，可以一次性执行完所有验证函数的逻辑
    if form.validate_on_submit():
        if form.data['flag'] == 'The homework is too difficult.':
            return 'Congratulations!'
        else:
            flash('有误')
            return 'Sorry, you are wrong.'
    return render_template("index.html", form = form)



if __name__ == '__main__':
    app.run(debug=True,port=5111)
