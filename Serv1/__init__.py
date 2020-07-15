import logging

import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letterstring = requests.get('http://localhost:7071/api/Serv2')
    nostring = requests.get('http://localhost:7071/api/Serv3')
    output = ""
    for i in range(5):
        output = output + letterstring[i-1]
        output = output + nostring[i-1]
    return func.HttpResponse(f"{output}")
