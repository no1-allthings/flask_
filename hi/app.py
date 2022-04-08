from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
def hi():
    return "hi ~ flask"

@app.route('/formhtml')
def formthml():
    return render_template('form.html')
    

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        num = request.args['num']
        name = request.args.get('name')
        return f"Get으로 {num} {name}  데이타 전달"
       
    elif request.method == "POST":
        num = request.form['num']
        name = request.form['name']
        return f"Post로 {num} {name}  데이터 전달"

@app.route('/hello/<name>')
def hello(name):
    return f"hell\ {name}"
@app.route('/input/<int:num>')
def input(num):
    name = ""
    if num == 1:
        name = "소현안녕"
    elif num == 2:
        name = "소현이쁘"
    return f"hi {name}"

@app.route('/myimg')
def myimg():
    return render_template('myimg.html')

@app.route('/y_yahoo')
def y_yahoo():
    return render_template('y_yahoo.html')
    
@app.route('/g_google')
def g_google():
    return redirect('https://www.google.com/')

@app.route('/urltest')
def url_test():
    return redirect(url_for('g_google'))  

@app.errorhandler(404)
def err404(error):
    return "404 에러", 404   

@app.route('/nopage')
def nopage():
    print('404로 보냅니다')
    abort(404)
    return "404로 보냅니다"
    
      

if __name__ == '__main__':    
   
    app.run(debug=True)