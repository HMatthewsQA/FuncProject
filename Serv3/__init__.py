import logging
import azure.functions as func
import random

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    nostring = ''.join(random.randint(0,10) for i in range(5))
    return func.HttpResponse(f"{nostring}")
