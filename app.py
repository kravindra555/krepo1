from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return("<h1>hello india</h1>")
@app.route('/<ravi>')
def hii(ravi):
    return render_template("hello.html",name=ravi)
if __name__ == "__main__":
    app.run(debug=True)
