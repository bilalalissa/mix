from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='frontend')

print("Frontend path:", os.path.join(app.root_path, 'frontend'))

shirts = [
    {"id": 1, "name": "Classic White Shirt", "price": "$20", "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Casual Blue Shirt", "price": "$25", "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Formal Black Shirt", "price": "$30", "image": "https://via.placeholder.com/150"}
]

@app.route('/api/shirts', methods=['GET'])
def get_shirts():
    return jsonify(shirts)

@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(app.root_path, 'frontend'), 'shirt_shopping.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3754, debug=True)
