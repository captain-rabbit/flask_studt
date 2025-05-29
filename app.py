from flask import Flask,render_template, request,redirect, url_for


app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


@app.route("/home")
def home():
    return "ok1111"

@app.route('/user/')
@app.route('/user/<username>')
def show_user(username=None):
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


if __name__ == '__main__':
    app.run()
    
