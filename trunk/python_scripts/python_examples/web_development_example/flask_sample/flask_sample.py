"""
Tips：
所有带@app装饰器的函数会自动调用，其他不带装饰器的函数必须手动调用才会执行

"""
# -*- coding:utf-8 -*-
from flask import Flask, Request, render_template, url_for

__author__ = 'Evan'
app = Flask(__name__, template_folder='templates')  # 初始化Flask，定义模板文件夹为"templates"


# 创建根目录
@app.route('/', methods=['GET', 'POST'])  # 路由根目录，配置访问方式：GET和POST均可访问
def root_directory():
    # 返回一个字符串到网页
    return "I'm root directory"


# 使用外部文件（外部文件会在template_folder定义的文件夹内查找）
@app.route('/display/')
def display_page():
    # 返回一个html页面
    return render_template('test.html')


# URL字段抓取（格式: <converter:variable_name>）
@app.route('/user/<username>/')
def ask_username(username):
    """
    URL字段抓取用法：
    @app.route('/user/<int:username>/')  # 抓取/user/后面的整形字段，如果不符合规则会报错
    @app.route('/user/<float:username>/')  # 抓取/user/后面的浮点形字段，如果不符合规则会报错
    @app.route('/user/<path:username>/')  # 抓取/user/后面的所有字段（包含/），如果不符合规则会报错
    :param username: 抓取/user/后面的所有字段（不包含/）赋值给username
    :return:
    """
    if username == 'Evan':
        return 'Welcome back'
    else:
        return "Hi {}".format(username)


# 使用url_for动态生成新的URL（原先的URL和更改后的URL都可以访问）
def generate_new_url():
    """
    url_for使用方法：
    param - endpoint: 接受函数名作为参数，为此函数生成新的URL
    param - **values: 接受函数内的形参作为参数，也接受未知变量名，未知变量名会添加到URL末尾作为查询参数
    :return:
    """
    with app.test_request_context():
        print(url_for(endpoint='display_page', username='Evan'))  # 生成新的URL：/display/?username=Evan
        print(url_for(endpoint='ask_username', username='Jane'))  # 生成新的URL：/user/Jane/


def main():
    # app.run(host='0.0.0.0')  # 使服务器可被网络内其他设备访问（不配置host，只能用本地电脑访问）
    app.run(debug=True)  # 启用Debug模式，服务器会在代码修改后自动重新载入（慎用，有安全隐患）


if __name__ == '__main__':
    main()
