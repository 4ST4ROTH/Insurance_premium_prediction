from crypt import methods
from flask import Flask , request

app = Flask(__name__)

@app.route("/home",methods=['GET','POST'])
def index():
    return "Starting machine learning project"

if __name__=="__main__":
    app.run(debug=True)