from flask import Flask
from scrapper import *

app = Flask(__name__)

@app.route("/<string:usn>/<string:date>/<string:month>/<string:year>")
def hello_world(usn,date,month,year):
    Login = SISLogin(usn,date,month,year)
    return get_data(Login[0],Login[1])

if __name__=='__main__':
    app.run(debug=True)