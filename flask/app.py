from flask import Flask, request, jsonify,render_template
## Web Server Gateway Interface
app = Flask(__name__)
 
@app.route("/")
def  welcome():
    return "Welcome to the Flask API"

@app.route("/index")
def index():
    if 
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form['name']
        return 'hello! {data}'.format(data=data)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)