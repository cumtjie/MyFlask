
from flask import Flask,url_for,request,render_template
import sys
sys.path.append('D:/MyCodeLab/MyFlask/MyCode/spider')
import MySpider

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return MySpider.requestCnblogs(1)
@app.route('/signin', methods=['GET'])
def signin_form():
    return MySpider.requestCnblogs(1)
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

@app.route("/id/<int:post_id>",methods=['GET','POST'])
def index(post_id):
    if request.method == 'POST':
        return 'POST:  my id is %d' % post_id
    else:
        return 'this is my first webSet  my id is %d' % post_id
    


 
if __name__ == '__main__':
    # app.debug = False
    app.run(host='localhost', port=5000)