# Put your app in here.
from flask import FLASK, request
from operations import add, sub, mult, div

app= Flask(__name__)

@app.route('/add')
def do_add():
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= add(a,b)
    return str(result)

@app.route('/subt')
def do_sub():
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= sub(a,b)
    return str(result)

@app.route('/mult')
def do_mult():
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= mult(a,b)
    return str(result)

@app.route("/divide")
def do_divide(a, b)
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= div(a,b)
    return str(result)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operator>")
"""returns math using the operation input by user"""
def do_math(operator):
    a= int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= operators[operator](a,b)
    return str(result)