from flask import Flask, Response, request, jsonify
import random
app = Flask(__name__)

animals = {'Cow':'Moo','Dog':'Woof', 'Cat':'Meow'}

@app.route('/')
@app.route('/info', methods=['GET'])
def get_text():
    return jsonify(random.choice(list(animals)))

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
