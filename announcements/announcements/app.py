from flask import request
from flask_lambda import FlaskLambda
import json
import boto3
ddb=boto3.resource('dynamodb')
app = FlaskLambda(__name__)

@app.route('/', methods=['GET'])
def list_announcements():
    table= ddb.Table('announcements')
    data= table.scan()['Items']
    return (
        json.dumps(data, indent=4, sort_keys=True),
        200,
        {'Content-Type': 'application/json'}
    )

@app.route('/add', methods=['GET','POST'])
def add_announcements():
    table= ddb.Table('announcements')
    table.put_item(Item=request.form.to_dict())
    return (
        json.dumps({"message":"announcement added"}),
        200,
        {'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    app.run(debug=True)