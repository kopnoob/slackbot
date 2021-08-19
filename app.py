from flask import Flask

app = Flask(__name__)

PORT = 4390

@app.route('/', methods=['POST'])
def homepage(timepris):
    #andel = 0.6
    #aga = 1/1.141
    #fp = 1/1.12
    #timer = 150
    #lonn=timepris*timer*andel*aga*fp
    return timepris


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
