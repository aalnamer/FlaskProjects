# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div  

app = Flask(__name__)

@app.route('/add')
def add_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a + b)
    return str(result)


@app.route('/sub')
def sub_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a - b)
    return str(result)
        
        
            
@app.route('/mult')
def mult_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a * b)
    return str(result)
              
              
@app.route('/div')
def div_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = (a / b)
    return str(result)
              
              
OP = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<operation>")

def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    result = OP[operation](a, b)
    return str(result)
