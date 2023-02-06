from types import MethodDescriptorType
import flask
from flask import jsonify, request
from flask import json
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

all_heroes = [ { 'id': 11, 'name': 'Dr Nice' },
   { 'id': 12, 'name': 'Dr. Dida' },
  { 'id': 13, 'name': 'Boss Julie' },
  { 'id': 14, 'name': 'Ann superwoman' },
  { 'id': 15, 'name': 'Kidula The Hulk' },
  { 'id': 16, 'name': 'virgin Mary' },
  { 'id': 17, 'name': 'Burning Moses' },
  { 'id': 18, 'name': 'Water Washington' },
  { 'id': 19, 'name': 'Magma George' },
  { 'id': 20, 'name': 'Tornado Trevor' }]

@app.route('/heroes', methods=['GET'])
def heroes():
    return jsonify(all_heroes)


@app.route('/detail/<id>' , methods=['Get'])
def detail(id):

  for x in all_heroes:
    print(x['id'])
    if int(x['id'])==int(id):
      return jsonify(x)


  return "Record not found", 404

  # update-post method
@app.route('/update', methods=['post'])
def update():

  data=request.data
  string= data.decode('UTF-8')
  # converting it to a dictionary
  data=eval(string) 
  print(data)

# this is to make it change in our list of heroes after rerunning the code it will return 
# to the original list of heroes since we dont have an actual database
  for x in all_heroes:
    if x['id'] == data['id']:
      x['name'] = data['name']
      return x

  return "Record Not Found", 400


app.run()