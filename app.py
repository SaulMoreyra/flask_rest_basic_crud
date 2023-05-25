from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!"})


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products})


@app.route('/products/<string:name>', methods=['GET'])
def getProduct(name: str):
    result = next(
        (product for product in products if product["name"] == name), None)
    if result is None:
        return jsonify({"message": "Not found"})
    return jsonify({"product": result})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "quantity": request.json["quantity"],
        "price": request.json["price"],
    }
    products.append(new_product)
    return jsonify({"product": new_product})


@app.route('/products/<string:name>', methods=['PUT'])
def editProduct(name: str):
    result = next(
        (product for product in products if product["name"] == name), None)
    if result is None:
        return jsonify({"message": "Not found"})

    newProduct = {
        "name": request.json["name"],
        "quantity": request.json["quantity"],
        "quantity": request.json["price"]
    }
    map(lambda product: newProduct if product["name"] == name else product)
    return jsonify({"product": result})


@app.route('/products/<string:name>', methods=['DELETE'])
def deleteProduct(name: str):
    result = next(
        (product for product in products if product["name"] == name), None)
    if result is None:
        return jsonify({"message": "Not found"})

    products.remove(result)
    return jsonify({"product": result})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
