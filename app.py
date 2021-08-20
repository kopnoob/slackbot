import re
from flask import Flask, request, Response

app = Flask(__name__)

PORT = 4390

@app.route('/', methods=['POST'])
def homepage():
    andel = 0.6
    aga = 1/1.141
    fp = 1/1.12

    inputs = request.form.get('text')
    splitInput = re.findall(r'[^,\s]+',inputs)

    timepris = splitInput[0]
    timer = splitInput[1]
    
    lonn = int(float(timepris)*float(timer)*andel*aga*fp)
    feedback = "{} timer med {} i timepris gir {} i lønn. Bonus og utbytte er også opparbeidet, og kommer i tillegg.".format(timer, timepris, lonn)
    
    return str(feedback)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
