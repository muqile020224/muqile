```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# API 1: 返回Hello World
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello World'})

# API 2: 返回传入的参数
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(data)

# API 3: 返回两个数的和
@app.route('/api/sum', methods=['POST'])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

# API 4: 返回传入的字符串的长度
@app.route('/api/length', methods=['POST'])
def length():
    data = request.get_json()
    text = data['text']
    length = len(text)
    return jsonify({'length': length})

# API 5: 返回传入的字符串的反转形式
@app.route('/api/reverse', methods=['POST'])
def reverse():
    data = request.get_json()
    text = data['text']
    reversed_text = text[::-1]
    return jsonify({'reversed_text': reversed_text})

if __name__ == '__main__':
    app.run(debug=True)