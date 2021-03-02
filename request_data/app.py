from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def api():
    r = request.args
    print(r)
    return {'sum' : int(r.get('a',0)) + int(r.get('b',0))}



@app.route('/index')
def home():
    path = request.path
    full_path = request.full_path
    root = request.script_root
    base_url = request.base_url
    url = request.url
    total = f'''
    <p> path:{path} </p>
    <p> full_path:{full_path} </p>
    <p> root :{bool(root)} </p>
    <p> base_url:{base_url} </p>
    <p> url:{url} </p>
    '''
    return total

app.run(debug=True)
