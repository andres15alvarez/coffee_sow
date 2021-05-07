from flask import Flask, request, jsonify
from flask_cors import CORS 
from marshmallow import Schema, fields, validate, ValidationError
from app.model import predict

app = Flask(__name__)
CORS(app)

class SowSchema(Schema):
    temperature = fields.Float(required=True, validate=validate.Range(min=0.0, max=50.0))
    humidity = fields.Float(required=True, validate=validate.Range(min=0.0, max=1.0))
    altitude = fields.Float(required=True, validate=validate.Range(min=0.0, max=5000.0))
    rain = fields.Float(required=True, validate=validate.Range(min=0.0, max=1000.0))
    sunshine = fields.Float(required=True, validate=validate.Range(min=0.0, max=24.0))

@app.route('/predict', methods=['POST'])
def make_prediction():
    data = request.get_json()
    print(data)
    try:
        data = SowSchema().load(data)
        y = predict(data['temperature'], data['humidity'], data['altitude'], data['rain'], data['sunshine'])
        return jsonify({'predict': 'Sow' if y else 'Not Sow'}), 200
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400 