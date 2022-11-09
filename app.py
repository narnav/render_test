from flask import Flask
app = Flask(__name__)

ar=[{"name":"betty","age":20}]

@app.route('/')
def hello():
    return f'Hello, World!{ar[0]}'
 
 
if __name__ == '__main__':
    app.run(debug=True)
