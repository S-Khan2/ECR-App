from flask import Flask, jsonify, render_template, request
import json
import boto3
import logging
from dotenv import load_dotenv
import os

def get_aws_client():
    aws_client = boto3.client('lambda',
                        region_name= os.getenv('region'),
                        aws_access_key_id=os.getenv('aws_access_key_id'),
                        aws_secret_access_key=os.getenv('aws_secret_access_key'))
    return aws_client

app = Flask(__name__, template_folder='templates')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        # send form_data to Lambda, get response
        return render_template('data.html',form_data = form_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
