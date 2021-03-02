  
from flask import Flask , render_template, request
from jinja2 import Template
from tinydb import TinyDB, Query
import json
db = TinyDB('db.json')
db.truncate()
table_specifications = db.table('specifications')
productQuery = Query()
app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    products = table_specifications.all()
    return render_template('home.html', products=products, productsCount=len(products))

@app.route('/product')
def product():
    r = request.args
    product = table_specifications.search(productQuery.ID == r.get('id',1))
    return render_template('product.html', product=product[0])


app.run(debug=True)