from flask import Flask, request, jsonify,render_template,redirect,url_for
## Web Server Gateway Interface
app = Flask(__name__)
 
@app.route("/")
def  welcome():
    return "Welcome to the Flask API"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form['name']
        return 'hello! {data}'.format(data=data)
    return render_template('index.html')
# varialbe rule

@app.route('/last/<int:total_score>')
def result(score):
    if score >= 50:
        return render_template("result.html",result = score,pass_fail = "Pass")
    else:
        return render_template("result.html",result = score,pass_fail = "Fail")

@app.route('/result',methods=['POST','GET'])
def success():
    total_score = 0

    if request.method == 'POST':

        maths = request.form['maths']
        science = request.form['science']
        history = request.form['history']
        english = request.form['english']
        total_score = int((int(maths) + int(science) + int(history) + int(english))/4)

        return redirect(url_for('last',score = total_score))
        

if __name__ == '__main__':
    app.run(debug=True)