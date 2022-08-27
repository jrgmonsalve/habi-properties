import json
import sys, os

from src.property.app import App


def handler(event, context):
    response = App.get_response(method=event["requestContext"]["http"]["method"],
                               path=event["requestContext"]["http"]["path"])

    # Get the current working directory
    cwd = os.getcwd()
    body = {}
    # Print the current working directory
    body["value1"] = "Current working directory: {0}".format(cwd)

    # Print the type of the returned object
    body["value2"] = "os.getcwd() returns an object of type: {0}".format(type(cwd))
    body["value3"]=[]
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        body["value3"].append(f)
    body["val4"]=response
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
