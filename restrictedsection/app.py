#!/usr/bin/env python
from flask import Flask, jsonify, request
from restricted_section import RestrictedSection
import json

app = Flask(__name__)

rs = RestrictedSection()

@app.route("/")
def home():
    """
    Home just returns a list of the KV store contents
    """
    return jsonify(rs.list())

@app.route("/insert", methods=['POST'])
def insert():
    """
    Insert values into the KV store
    """
    response = {
            "message": "insert successful",
            "status": 200
    }

    data_dict = request.json
    
    if len(data_dict) > 1:
        response["message"] = "error: more than one key-value pair supplied"
        response["status"] = 400
        return jsonify(response), 400

    for key, value in data_dict.items():
        try:
            rs.insert(key, value)
        except Exception as ex:
            response["message"] = "error during key-value insertion"
            response["status"] = 500
            return jsonify(response), 500

    return jsonify(response)

@app.route("/get/<key>", methods=['GET'])
def get(key):
    """
    Retrieve a value from the key-value store
    """
    response = {
            "message": "retrieval successful",
            "key": str(key),
            "value": "",
            "status": 200
    }
    value = rs.get(key)
    if not value:
        response["message"] = f"key: {key} does not exist in key-value store"
        response["status"] = 400
        return jsonify(response)
    
    response["value"] = value
    return jsonify(response)

@app.route("/delete", methods=['DELETE'])
def delete():
    """
    Deletes a key-value pair from the KV store
    """
    response = {
            "message": "deletion successful",
            "status": 200
    }

    data_dict = request.json

    if len(data_dict) > 1:
        response["message"] = "error: more than one key-value pair supplied"
        response["status"] = 400
        return jsonify(response)

    for key, value in data_dict.items():
        if rs.delete(key):
            return jsonify(response)
        else:
            response["message"] = "error preforming deletion, please try again later"
            rseponse["status"] = 500
            return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
