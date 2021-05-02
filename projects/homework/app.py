from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

# 로컬 클라이언트, 로컬서버 몽고DB
# client = MongoClient('localhost', 27017)
# db = client.dbsparta

# 로컬 클라이언트, 원격서버 몽고 DB
# client = MongoClient('mongodb://web1mhz:web1024@183.111.227.18', 27017)
# db = client.remotesparta

# 원격 클라이언트, 원격 서버몽고 DB
client = MongoClient('mongodb://web1mhz:web1024@localhost', 27017)
db = client.remotesparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():

    name = request.form['name']
    quantity = request.form['quantity']
    address = request.form['address']
    phone = request.form['phone']

    print(name)

    doc = {
        'name': name,
        'quantity': quantity,
        'address': address,
        'phone': phone
    }

    db.order_product.insert_one(doc)

    return jsonify({"성공":"저장완료했습니다."})

@app.route('/order_list', methods=['GET'])
def order_list():

    order_list = list(db.order_product.find({},{'_id':False}))

    return jsonify({"order_product": order_list})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)