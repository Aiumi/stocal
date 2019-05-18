from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('firstcopy.html', 'r') as myfile:
        data = myfile.read().replace('\n', '')
        return data

if __name__ == '__main__':
    app.run()
