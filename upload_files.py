import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

BLOB_CONNECTION_STRING = ""
CONTAINER_NAME = ""
EXTENSION = ""

images = [x for x in os.listdir('.') if EXTENSION in x]

blob_service_client =  BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)
for image in images:
    with open(image, 'rb') as file:
        container_client.upload_blob(image, file.read())