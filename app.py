from re import split
from flask import Flask, request, Response

app = Flask(__name__)

PORT = 4390

@app.route('/', methods=['POST'])
def homepage():
    andel = 0.6
    aga = 1/1.141
    fp = 1/1.12
    #timer = 150

    inputs = request.form.get('text')
    splitInput = inputs.split(",")

    timepris = splitInput[0]
    timer = splitInput[1]
    
    lonn = int(float(timepris)*float(timer)*andel*aga*fp)
    
    return str(lonn)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
