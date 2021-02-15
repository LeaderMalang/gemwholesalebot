from flask import Flask,render_template,request,jsonify
from db import con
app = Flask(__name__)


@app.route('/_getListing')
def getListing():
    a = request.args.get('draw', 0)
    b = request.args.get('start', 0)
    return jsonify(result=a + b)


@app.route('/')
def hello():



    return render_template('index.html')

if __name__ == '__main__':
    app.run()