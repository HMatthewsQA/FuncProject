import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letterstring = requests.get('https://hmatthewsserverless.azurewebsites.net/api/Serv2?code=MRsXjiyVcTd9I7A73UQRunNhpjVXpmm4y6SX0fHladqS1CDNkAjnFg==').text
    
    nostring = requests.get('https://hmatthewsserverless.azurewebsites.net/api/Serv3?code=U0/1jOcnDSmZsTX/cb/n91W3Z57dArm6IcjpOVarOI9L1QOZh6gvaw==').text
    
    username = ""
    for i in range(5):
        username += letterstring[i]
        username += nostring[i]
    
    endpoint = "https://hmatthews-serverless.documents.azure.com:443/"
    key = "TqGtmOd1GqzEDaI36da2FbCnuhYsRmRnQ9hVyx8PMbsuuBuQCCjJ6bcNu3gx5MTNRACTtpBiubj15rLeS6hPmA=="
    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    client.create_database_if_not_exists(id=database_name)

    container_name = "UsernameContainer"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username")
    )
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)

    return username
