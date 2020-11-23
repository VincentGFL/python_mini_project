from flask import Flask, Response, request, jsonify
import random
app = Flask(__name__)

animals = {'Cow':'Moo','Dog':'Woof', 'Cat':'Meow'}

print('HTTP GET Request (json):')
response = requests.get(api + '/info')
print('Whole Response: ' + str(response.json()))
print('"data" Property of the Response: ' +  str(response.json()["data"]))

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
