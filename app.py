import json
from flask import Flask
app = Flask(__name__)

ar=[{"name":"betty","age":20},{"name":"alex","age":21},{"name":"shadi","age":15}]

@app.route('/')
def hello():
    return json.dumps( ar)
 
 
if __name__ == '__main__':
    app.run(debug=True)
