import json

from flask import Flask, request

from middleware.yml import read_yaml, write_yaml
from middleware.res import res_data

app = Flask(__name__)

""" 定义简单的接口用于测试，没用做完整的参数和逻辑校验  """


# 登录接口
@app.route('/signin', methods=['POST'])
def sign_in():
    req_data = dict(json.loads(request.data))
    fields = req_data.keys()

    if 'account' not in fields or 'password' not in fields:
        return res_data(40001, '缺少必要的参数', None)

    account = req_data['account']
    password = req_data['password']

    if account == '' or password == '':
        return res_data(40002, '账号密码不能为空', None)

    user_db = dict(read_yaml('fake_db/user_db.yaml'))

    if user_db.get(account) is None:
        return res_data(40003, '账号不存在', None)

    if user_db[account]['password'] != password:
        return res_data(40004, '登录失败，密码错误', None)

    if user_db[account]['password'] == password:
        return res_data(20000, '登录成功', {'token': 'fake@token'})


# 注册接口
@app.route('/signup', methods=['POST'])
def sign_up():
    req_data = dict(json.loads(request.data))
    fields = req_data.keys()

    if 'account' not in fields or 'password' not in fields:
        return res_data(40001, '缺少必要的参数', None)

    account = req_data['account']
    password = req_data['password']

    if account == '' or password == '':
        return res_data(40002, '账号密码不能为空', None)

    if len(account) < 8 or len(account) > 18:
        return res_data(40003, '账号长度不符合规则', None)

    if len(password) < 8 or len(password) > 18:
        return res_data(40003, '密码长度不符合规则', None)

    user_db = dict(read_yaml('fake_db/user_db.yaml'))

    if user_db.get(account) is not None:
        return res_data(40004, '账号已存在', None)

    if user_db.get(account) is None:
        new_user = {
            account: {
                'account': str(account),
                'password': str(password)
            }
        }
        write_yaml('fake_db/user_db.yaml', new_user)
        return res_data(20000, '账号注册成功', None)


app.run(debug=True)