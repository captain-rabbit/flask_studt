from flask import Flask, make_response,render_template, request,redirect, url_for,json,jsonify


app = Flask(__name__)



@app.route('/')
@app.route('/index')
@app.route('/flask/')
@app.route('/flask/index')
def index():
    return render_template('home.html')


@app.route("/flask/home")
def home():
    return "ok1111"

@app.route('/user/')
@app.route('/user/<username>')
def show_user(username):
    age = request.args.get("age",'nil')
    return render_template('user.html',username = username,age = age)

@app.route("/blog/list")
def blog_list():
    page=request.args.get('page',default=1,type=int)
    size=request.args.get('size',default=10,type=int)
    print(page,size)
    return f'博客列表第{page}页,这一页有{size}条数据'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')
        return redirect(url_for('show_user', username=username, age=age))
    return render_template('form.html')

#测试hook 
@app.route("/test_hook")
def test_hook():
    print("do_something")
    # a=1/0
    return "ok"

@app.before_request
def do_something_befor():
    print("requesr_befor",request.url)
#异常处理
@app.teardown_request
def do_something_teardown(excetion):
    print("requesr_teardown",excetion,request.url)

@app.after_request
def do_something_after(response):
    print("requesr_after",request.url)
    return response

#重定向
@app.route('/bili')
def bili():
    return redirect('https://www.bilibili.com/')

#响应格式
@app.route('/rejson')
def rejson():
    data={
        'name':'heys',
        'age':'101'
    }
    # response=make_response(json.dumps(data))     #make_response手动构建一个http响应对象
    # response.mimetype='application/json'         #设置响应头中的 Content-Type 为 application/json。
    return jsonify(data)

if __name__ == '__main__':
    app.run()



#http://192.168.1.15/
    
